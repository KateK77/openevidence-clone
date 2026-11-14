param([int]$BackendPort = 8021, [int]$FrontendPort = 5173)
$ErrorActionPreference = 'Stop'
$projectRoot = $PSScriptRoot
. (Join-Path $projectRoot 'scripts\runtime.ps1')
$pythonPath = Find-ProjectPython $projectRoot
$nodePath = Find-ProjectNode
$runtimeDirectory = Join-Path $projectRoot '.runtime'
New-Item -ItemType Directory -Path $runtimeDirectory -Force | Out-Null
if (!(Test-Path -LiteralPath (Join-Path $projectRoot '.env'))) {
    Copy-Item -LiteralPath (Join-Path $projectRoot '.env.example') -Destination (Join-Path $projectRoot '.env')
}
$managePath = Join-Path $projectRoot 'backend\manage.py'
$vitePath = Join-Path $projectRoot 'frontend\node_modules\vite\bin\vite.js'
if (!(Test-Path -LiteralPath $vitePath)) { throw 'Frontend dependencies are missing. Run setup.ps1 first.' }
& $pythonPath $managePath backup_local
if ($LASTEXITCODE -ne 0) { throw 'Database backup failed; startup stopped before migration.' }
& $pythonPath $managePath migrate --noinput
if ($LASTEXITCODE -ne 0) { throw 'Database migration failed.' }
$backendUrl = "http://127.0.0.1:$BackendPort"
$frontendUrl = "http://127.0.0.1:$FrontendPort"
$env:BACKEND_URL = $backendUrl
$env:DJANGO_CSRF_TRUSTED_ORIGINS = "$frontendUrl http://localhost:$FrontendPort"
$newProcesses = @()
try {
    if (Test-LocalPort $BackendPort) {
        $health = Invoke-RestMethod "$backendUrl/api/health/" -TimeoutSec 5
        if ($health.service -ne 'medevidence' -or $health.version -ne '2.0.0') {
            throw "Port $BackendPort belongs to another service or version. Choose -BackendPort with a free port."
        }
        Write-Host "MedEvidence backend is already running at $backendUrl"
    } else {
        $quotedManage = '"' + $managePath + '"'
        $process = Start-Process -FilePath $pythonPath -ArgumentList @($quotedManage, 'runserver', "127.0.0.1:$BackendPort", '--noreload') -WorkingDirectory $projectRoot -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runtimeDirectory 'backend.log') -RedirectStandardError (Join-Path $runtimeDirectory 'backend-error.log')
        $newProcesses += $process
    }
    $backendReady = $false
    for ($attempt = 0; $attempt -lt 40; $attempt++) {
        try {
            $health = Invoke-RestMethod "$backendUrl/api/health/" -TimeoutSec 2
            if ($health.service -eq 'medevidence' -and $health.version -eq '2.0.0') { $backendReady = $true; break }
        } catch {}
        Start-Sleep -Milliseconds 250
    }
    if (!$backendReady) { throw 'Backend did not become ready. Inspect .runtime/backend-error.log.' }
    if (Test-LocalPort $FrontendPort) {
        $page = Invoke-WebRequest $frontendUrl -UseBasicParsing -TimeoutSec 5
        if ($page.Content -notmatch '<title>MedEvidence AI') {
            throw "Port $FrontendPort belongs to another service. Choose -FrontendPort with a free port."
        }
        $proxyHealth = Invoke-RestMethod "$frontendUrl/api/health/" -TimeoutSec 5
        if ($proxyHealth.service -ne 'medevidence' -or $proxyHealth.version -ne '2.0.0' -or $proxyHealth.port -ne "$BackendPort") {
            throw 'The existing frontend has a different API target. Restart that frontend before continuing.'
        }
        Write-Host "MedEvidence frontend is already running at $frontendUrl"
    } else {
        $quotedVite = '"' + $vitePath + '"'
        $process = Start-Process -FilePath $nodePath -ArgumentList @($quotedVite, '--host', '127.0.0.1', '--port', "$FrontendPort", '--strictPort') -WorkingDirectory (Join-Path $projectRoot 'frontend') -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runtimeDirectory 'frontend.log') -RedirectStandardError (Join-Path $runtimeDirectory 'frontend-error.log')
        $newProcesses += $process
    }
    $ready = $false
    for ($attempt = 0; $attempt -lt 40; $attempt++) {
        try {
            $health = Invoke-RestMethod "$frontendUrl/api/health/" -TimeoutSec 2
            if ($health.service -eq 'medevidence' -and $health.version -eq '2.0.0') { $ready = $true; break }
        } catch {}
        Start-Sleep -Milliseconds 250
    }
    if (!$ready) { throw "Startup did not finish. Inspect logs in $runtimeDirectory." }
    if ($newProcesses.Count) {
        $statePath = Join-Path $runtimeDirectory 'processes.json'
        $previous = @()
        if (Test-Path -LiteralPath $statePath) { $previous = @(Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json) }
        $records = @($previous) + @($newProcesses | ForEach-Object { @{pid=$_.Id; started=$_.StartTime.ToUniversalTime().ToString('o'); project=$projectRoot} })
        ConvertTo-Json -InputObject @($records) | Set-Content -LiteralPath $statePath -Encoding UTF8
    }
    Write-Host "MedEvidence AI 2.0 is ready: $frontendUrl"
    Write-Host 'Run stop.ps1 to stop only processes started by this launcher.'
} catch {
    foreach ($process in $newProcesses) {
        if (Get-Process -Id $process.Id -ErrorAction SilentlyContinue) { & taskkill.exe /PID $process.Id /T /F | Out-Null }
    }
    throw
}
