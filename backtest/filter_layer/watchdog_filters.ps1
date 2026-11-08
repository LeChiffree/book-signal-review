$ErrorActionPreference = 'SilentlyContinue'
$bt = 'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
$py = 'C:\Users\GIGABAYT\AppData\Local\Programs\Python\Python311\python.exe'
$trades = Join-Path $bt 'filter_layer\results\trades'
$log = Join-Path $bt 'filter_layer\run_filters.watchdog.out.log'
$err = Join-Path $bt 'filter_layer\run_filters.watchdog.err.log'

while ($true) {
    $n = (Get-ChildItem $trades -Filter *.parquet | Measure-Object).Count
    if ($n -ge 525) { break }
    $running = @(Get-CimInstance Win32_Process -Filter "name='python.exe'" |
        Where-Object { $_.CommandLine -like '*filter_layer\run_filters.py*' })
    if ($running.Count -gt 0) {
        $ids = @($running | ForEach-Object { $_.ProcessId })
        $kids = @(Get-CimInstance Win32_Process -Filter "name='python.exe'" |
            Where-Object { $ids -contains $_.ParentProcessId })
        if ($kids.Count -eq 0) {
            $running | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
            $running = @()
        }
    }
    if ($running.Count -eq 0) {
        Start-Process -FilePath $py `
            -ArgumentList @('-u', (Join-Path $bt 'filter_layer\run_filters.py'), '--workers', '12') `
            -WorkingDirectory $bt `
            -RedirectStandardOutput $log `
            -RedirectStandardError $err `
            -WindowStyle Hidden | Out-Null
    }
    Start-Sleep -Seconds 300
}
