$ErrorActionPreference = 'Stop'
$bt = 'D:\Paper_ML_BSH\analysis\book_signal_review\backtest\filter_layer'
$py = 'C:\Users\GIGABAYT\AppData\Local\Programs\Python\Python311\python.exe'
$log = Join-Path $bt 'finalize_v2.log'

while (Get-Process -Id 11412 -ErrorAction SilentlyContinue) { Start-Sleep -Seconds 10 }
Start-Sleep -Seconds 5
"finalize v2 start $(Get-Date -Format o)" | Out-File $log -Encoding utf8
& $py -u (Join-Path $bt 'build_filter_dashboard_v2.py') *>> $log
& $py -u (Join-Path $bt 'report_filters.py') *>> $log
"finalize v2 done $(Get-Date -Format o)" | Out-File $log -Append -Encoding utf8
