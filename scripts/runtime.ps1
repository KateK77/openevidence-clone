function Find-ProjectPython {
    param([string]$ProjectRoot)
    foreach ($candidate in @((Join-Path $ProjectRoot '.venv\Scripts\python.exe'), (Join-Path $ProjectRoot '..\..\work\venv\Scripts\python.exe'))) {
        if (Test-Path -LiteralPath $candidate) { return (Resolve-Path -LiteralPath $candidate).Path }
    }
    throw 'Python dependencies are not installed. Run setup.ps1 first.'
}
function Find-ProjectNode {
    $command = Get-Command node -ErrorAction SilentlyContinue
    if ($command) { return $command.Source }
    if (Get-Command Get-AppxPackage -ErrorAction SilentlyContinue) {
        foreach ($package in (Get-AppxPackage -Name 'OpenAI.CodexPrimaryRuntime*' -ErrorAction SilentlyContinue)) {
            $candidate = Join-Path $package.InstallLocation 'dependencies\node\bin\node.exe'
            if (Test-Path -LiteralPath $candidate) { return $candidate }
        }
    }
    throw 'Node.js was not found. Install Node.js 24 LTS, reopen PowerShell, and run setup.ps1.'
}
function Test-LocalPort {
    param([int]$Port)
    $socket = New-Object System.Net.Sockets.TcpClient
    try { return $socket.ConnectAsync('127.0.0.1', $Port).Wait(700) -and $socket.Connected }
    catch { return $false }
    finally { $socket.Dispose() }
}
