$ErrorActionPreference = 'SilentlyContinue'
$bt = 'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
$py = 'C:\Users\GIGABAYT\AppData\Local\Programs\Python\Python311\python.exe'
$summary = Join-Path $bt 'results_525\summary'
$log = Join-Path $bt 'run_525_watchdog.out.log'
$err = Join-Path $bt 'run_525_watchdog.err.log'

while ($true) {
    $n = (Get-ChildItem $summary -Filter *.parquet | Measure-Object).Count
    if ($n -ge 525) { break }
    $running = @(Get-CimInstance Win32_Process -Filter "name='python.exe'" |
        Where-Object { $_.CommandLine -like '*run_all_525.py*' })
    if ($running.Count -gt 0) {
        $ids = @($running | ForEach-Object { $_.ProcessId })
        $kids = @(Get-CimInstance Win32_Process -Filter "name='python.exe'" |
            Where-Object { $ids -contains $_.ParentProcessId })
        if ($kids.Count -eq 0) {
            # A runner with no workers is hung after a broken pool; clear it.
            $running | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
            $running = @()
        }
    }
    if ($running.Count -eq 0) {
        Start-Process -FilePath $py `
            -ArgumentList @('-u', (Join-Path $bt 'run_all_525.py'), '--workers', '12') `
            -WorkingDirectory $bt `
            -RedirectStandardOutput $log `
            -RedirectStandardError $err `
            -WindowStyle Hidden | Out-Null
    }
    Start-Sleep -Seconds 300
}
