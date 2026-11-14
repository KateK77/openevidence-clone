$ErrorActionPreference = 'Stop'
$statePath = Join-Path $PSScriptRoot '.runtime\processes.json'
if (!(Test-Path -LiteralPath $statePath)) { Write-Host 'No launcher-owned processes were recorded.'; return }
$records = @(Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json)
foreach ($record in $records) {
    $process = Get-Process -Id $record.pid -ErrorAction SilentlyContinue
    if ($process -and $record.project -eq $PSScriptRoot -and $process.StartTime.ToUniversalTime().Ticks -eq ([datetime]$record.started).ToUniversalTime().Ticks) {
        # Windows virtual-environment Python launches a child interpreter.
        & taskkill.exe /PID $process.Id /T /F | Out-Null
        if ($LASTEXITCODE -ne 0) { throw "Could not stop process tree $($process.Id)." }
        Write-Host "Stopped MedEvidence process $($process.Id)"
    }
}
Set-Content -LiteralPath $statePath -Value '[]' -Encoding UTF8
