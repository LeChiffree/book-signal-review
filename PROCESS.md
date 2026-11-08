# Üç kitaplık okuma hedefi

Kullanıcı bu sohbeti her devam ettirdiğinde `BOOK_LOG.csv` içindeki `read_status=complete` kitaplar atlanır ve arşivden henüz tamamlanmamış **üç PDF** seçilir. Her kitabın bütün PDF sayfaları okunur; metin çıkmayan kritik şekil/tablo sayfaları görsel incelenir. Bir kitap OCR gerektiriyorsa sıradaki kitaba sessizce geçilmez; durum kayda yazılır ve mümkünse OCR ile tamamlanır.

Her partide `batch_NNN/STRATEGIES.md` içine şu bilgiler yazılır: tam kaynak ve PDF sayfaları, kitabın asıl kuralı, kripto günlük karar sözleşmesine uyarlama, önceki kapanmış mumlarla tanımlı olay, sayısal özellikler, giriş/çıkış/stop adayları, belirsizlikler ve ertelenen fikirler. Kitap örnekleri kârlılık kanıtı sayılmaz. Backtest ve paper test ayrıca istenip uygulandığında sonucu farklı dosyada kaydedilir.

Sıra numarası ve tamamlanma durumu `BOOK_LOG.csv` içinde tutulur. Mevcut günlük strateji sözleşmesi `research_v2/24_MULTIDAY_STRATEGY_CONTRACT.md` esas alınır; yeni sinyal, var olan 1.300 özelliklik pilotta eşdeğeri varsa tekrar sütun olarak önerilmez.
