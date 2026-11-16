param([string]$Model = 'gemini-3.5-flash-lite')
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'scripts\runtime.ps1')
$pythonPath = Find-ProjectPython $PSScriptRoot
& $pythonPath (Join-Path $PSScriptRoot 'backend\manage.py') configure_model --model $Model
if ($LASTEXITCODE -ne 0) { throw 'Model configuration did not complete.' }
