param()
$ErrorActionPreference = 'Stop'
$manifest = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'SHA256.json') -Raw | ConvertFrom-Json
foreach ($entry in $manifest.files) {
    $rel = [string]$entry.path
    if ($rel -notmatch '^[A-Za-z0-9_.-]+$') { throw 'Invalid package entry path.' }
    $file = Join-Path $PSScriptRoot $rel
    $hash = (Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($hash -ne $entry.sha256) { throw "Hash mismatch: $rel" }
}
Write-Output ('Package hashes verified: ' + @($manifest.files).Count + ' files.')
