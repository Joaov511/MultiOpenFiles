$scriptRoot = $PSScriptRoot
$paths = Join-Path $scriptRoot "paths.txt"

Get-Content -Path $paths | ForEach-Object {
    Start-Process -FilePath "$_" #
}

