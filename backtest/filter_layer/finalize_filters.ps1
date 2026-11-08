$ErrorActionPreference = 'Stop'
$bt = 'D:\Paper_ML_BSH\analysis\book_signal_review\backtest'
$py = 'C:\Users\GIGABAYT\AppData\Local\Programs\Python\Python311\python.exe'
$trades = Join-Path $bt 'filter_layer\results\trades'
$log = Join-Path $bt 'filter_layer\finalize_filters.log'

while ($true) {
    $n = (Get-ChildItem $trades -Filter *.parquet | Measure-Object).Count
    $running = @(Get-CimInstance Win32_Process -Filter "name='python.exe'" |
        Where-Object { $_.CommandLine -like '*filter_layer\run_filters.py*' })
    if ($n -ge 525 -and $running.Count -eq 0) { break }
    Start-Sleep -Seconds 120
}
Start-Sleep -Seconds 30
"finalize start $(Get-Date -Format o)" | Out-File $log -Encoding utf8
& $py -u (Join-Path $bt 'filter_layer\aggregate_filters.py') *>> $log
if ($LASTEXITCODE -eq 0) {
    & $py -u (Join-Path $bt 'filter_layer\build_filter_dashboard.py') *>> $log
    & $py -u (Join-Path $bt 'filter_layer\report_filters.py') *>> $log
}
"finalize done $(Get-Date -Format o)" | Out-File $log -Append -Encoding utf8
