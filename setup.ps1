$ErrorActionPreference = 'Stop'
$projectRoot = $PSScriptRoot
. (Join-Path $projectRoot 'scripts\runtime.ps1')
$nodePath = Find-ProjectNode
try { $pythonPath = Find-ProjectPython $projectRoot }
catch {
    $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
    if (!$pythonCommand) { throw 'Install Python 3.12 or later, then reopen PowerShell.' }
    & $pythonCommand.Source -m venv (Join-Path $projectRoot '.venv')
    if ($LASTEXITCODE -ne 0) { throw 'Could not create the Python environment.' }
    $pythonPath = Find-ProjectPython $projectRoot
}
& $pythonPath -m pip install -r (Join-Path $projectRoot 'backend\requirements.txt')
if ($LASTEXITCODE -ne 0) { throw 'Python dependency installation failed.' }
Push-Location (Join-Path $projectRoot 'frontend')
try {
    $npmCommand = Get-Command npm.cmd -ErrorAction SilentlyContinue
    $workspaceNpm = Join-Path $projectRoot '..\..\work\npm\package\bin\npm-cli.js'
    if ($npmCommand) { & $npmCommand.Source ci }
    elseif (Test-Path -LiteralPath $workspaceNpm) { & $nodePath $workspaceNpm ci }
    else { throw 'npm was not found. Install Node.js 24 LTS with npm and reopen PowerShell.' }
    if ($LASTEXITCODE -ne 0) { throw 'Frontend dependency installation failed.' }
} finally { Pop-Location }
Write-Host 'Dependencies are ready. Run .\start.ps1'
