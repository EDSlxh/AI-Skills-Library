param(
    [string]$Root = ('D:\AI-Home\Fresh-' + (Get-Date -Format 'yyyyMMdd-HHmmss')),
    [switch]$Apply
)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$fullRoot = [IO.Path]::GetFullPath($Root)
if ($fullRoot -notmatch '^D:\\AI-Home\\Fresh-[A-Za-z0-9_-]+$') {
    throw 'Use a NEW D:\AI-Home\Fresh-<name> directory. Existing staged projects are not overwritten.'
}
if (Test-Path -LiteralPath $fullRoot) { throw 'Destination exists. Choose a new Fresh-<name> directory.' }
$source = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'sources.json') -Raw | ConvertFrom-Json
$revision = [string]$source.library.local_commit
if ($revision -notmatch '^[0-9a-f]{40}$') { throw 'Invalid recorded revision.' }
if (-not $Apply) {
    Write-Output "Preview: clone the public skill library at $revision into $fullRoot."
    Write-Output 'Create D-drive cache directories and a process-only environment script.'
    Write-Output 'No apps, models, dependencies or personal projects will be restored automatically.'
    Write-Output 'No existing files, settings, credentials or C-drive files will be changed.'
    Write-Output 'To execute this narrow restore, run this script with -Apply.'
    return
}
$gitExe = Get-Command git -CommandType Application -ErrorAction Stop | Select-Object -First 1
New-Item -ItemType Directory -Path $fullRoot | Out-Null
foreach ($rel in @('Projects','Cache\uv','Cache\npm','Cache\pip','Models\huggingface','Runtimes\uv-python')) {
    New-Item -ItemType Directory -Path (Join-Path $fullRoot $rel) | Out-Null
}
$repo = Join-Path $fullRoot 'Projects\AI-Skills-Library'
& $gitExe.Source clone --no-checkout 'https://github.com/EDSlxh/AI-Skills-Library.git' $repo
if ($LASTEXITCODE -ne 0) { throw 'Git clone failed; C originals were not changed. Pick another new destination to retry.' }
& $gitExe.Source -C $repo checkout --detach $revision
if ($LASTEXITCODE -ne 0) { throw 'Could not check out the recorded revision.' }
$actual = & $gitExe.Source -C $repo rev-parse HEAD
if ($LASTEXITCODE -ne 0 -or $actual.Trim() -ne $revision) { throw 'Restored revision mismatch.' }
$environment = @'
$recoveryRoot = $PSScriptRoot
$env:UV_CACHE_DIR = Join-Path $recoveryRoot 'Cache\uv'
$env:UV_PYTHON_INSTALL_DIR = Join-Path $recoveryRoot 'Runtimes\uv-python'
$env:npm_config_cache = Join-Path $recoveryRoot 'Cache\npm'
$env:PIP_CACHE_DIR = Join-Path $recoveryRoot 'Cache\pip'
$env:HF_HOME = Join-Path $recoveryRoot 'Models\huggingface'
$env:CLAUDE_SKILL_DIR = Join-Path $recoveryRoot 'Projects\AI-Skills-Library\ai-skills\07-geolocation\geo-sleuth'
Write-Output "Recovery process caches set under $recoveryRoot"
'@
Set-Content -LiteralPath (Join-Path $fullRoot 'Environment.ps1') -Value $environment -Encoding UTF8
Write-Output "Public skill sources restored at $repo ($revision)."
Write-Output "In a PowerShell session: . '$fullRoot\Environment.ps1'"
Write-Output 'These variables affect that shell and its child processes only; the desktop app is not reconfigured.'
Write-Output 'Personal projects, local geo overrides, plugins, models and histories require the separate steps in RESTORE.md.'
Write-Output 'No C-drive space has been freed by this script.'
