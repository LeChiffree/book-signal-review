$ErrorActionPreference = 'Stop'
$bt = 'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
$py = 'C:\Users\GIGABAYT\AppData\Local\Programs\Python\Python311\python.exe'
$summary = Join-Path $bt 'results_525\summary'
$log = Join-Path $bt 'finalize_525.log'

while ($true) {
    $n = (Get-ChildItem $summary -Filter *.parquet | Measure-Object).Count
    $running = @(Get-CimInstance Win32_Process -Filter "name='python.exe'" |
        Where-Object { $_.CommandLine -like '*run_all_525.py*' })
    if ($n -ge 525 -and $running.Count -eq 0) { break }
    Start-Sleep -Seconds 120
}
Start-Sleep -Seconds 30
"finalize start $(Get-Date -Format o)" | Out-File $log -Encoding utf8
& $py -u (Join-Path $bt 'aggregate_525.py') *>> $log
& $py -u (Join-Path $bt 'build_dashboard.py') *>> $log
& $py -u (Join-Path $bt 'build_report.py') *>> $log
"finalize done $(Get-Date -Format o)" | Out-File $log -Append -Encoding utf8
