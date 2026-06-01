# AI Yönetici Yorumu

## 1. Kısa Yönetici Özeti

Bu rapora göre toplam satış tutarı **67.700.256 TL**, kazanılan satış toplamı ise **22.744.126 TL** olarak hesaplanmıştır. Satış hacminde **Antalya** bölgesi, ürün bazında **Paket C**, satış temsilcisi bazında ise **Burak** öne çıkmaktadır.

Ancak raporda **8 veri kalite problemi** ve **21 riskli müşteri kaydı** bulunduğu için bu sonuçlar doğrudan nihai karar için kullanılmamalıdır. Önce veri temizliği ve riskli kayıtların kontrolü yapılmalıdır.

## 2. Dikkat Edilmesi Gereken Ana Riskler

Bu veri setinde öne çıkan riskler; anormal yüksek satış, negatif satış tutarı, durum/ödeme tutarsızlığı, eksik satış tutarı, hatalı tarih, geciken ödeme kayıtlarıdır. Bu problemler hem toplam satış rakamını hem de bölge/temsilci performansını etkileyebilir.

Öncelikli riskli müşteriler:

- **Nova Teknoloji** (Yüksek, skor: 11): Geciken ödeme + Durum/ödeme tutarsızlığı + Anormal yüksek satış — Tahsilat takip listesine alınmalı; kayıt satış veya finans ekibi tarafından kontrol edilmeli; gerçek satışsa stratejik müşteri olarak takip edilmeli; hataysa düzeltilmeli.
- **Mira Perakende** (Yüksek, skor: 7): Geciken ödeme + Negatif satış tutarı — Tahsilat takip listesine alınmalı; finans/muhasebe ekibi bu kaydı doğrulamalı.
- **Eksen Otomotiv** (Yüksek, skor: 6): Eksik satış tutarı + Geciken ödeme — Tutar bilgisi tamamlanmadan rapor hesaplamasına güvenilmemeli; tahsilat takip listesine alınmalı.
- **Star Medya** (Yüksek, skor: 5): Geciken ödeme + Hatalı tarih — Tahsilat takip listesine alınmalı; tarih düzeltilmeden dönemsel analiz yapılmamalı.
- **Akdeniz Turizm** (Düşük, skor: 2): Geciken ödeme — Tahsilat takip listesine alınmalı.

## 3. Satış Performansı Yorumu

Bölge bazında ilk üç satış hacmi:

- **Antalya**: 14.420.409 TL
- **Ankara**: 11.777.147 TL
- **İstanbul**: 11.311.584 TL

Ürün bazında satış hacmi:

- **Paket C**: 26.129.817 TL
- **Paket B**: 21.895.718 TL
- **Paket A**: 19.674.721 TL

Satışın büyük kısmı **Paket C** üzerinde yoğunlaşmış görünüyor. Ancak **Nova Teknoloji** gibi anormal yüksek satış içeren kayıtlar toplam performansı şişiriyor olabilir. Bu nedenle yüksek tutarlı satışlar ayrıca doğrulanmalıdır.

Beklemede olan **163 satış** için hızlı takip yapılması, kısa vadede satışa dönüş potansiyeli yaratabilir. Kaybedilen **175 satış** için de kayıp nedeni analizi standart hale getirilmelidir.

## 4. Öncelikli Aksiyon Planı

1. Eksik, negatif ve hatalı tarih içeren kayıtlar düzeltilmeden nihai rapor kullanılmamalı.
2. Geciken ödemeler için tahsilat takip listesi oluşturulmalı.
3. Anormal yüksek satışlar gerçek mi veri hatası mı kontrol edilmeli.
4. Beklemede olan satışlar için satış temsilcileri hızlı takip yapmalı.
5. Durum alanı Kazanıldı, Beklemede, Kaybedildi değerleriyle standartlaştırılmalı.

## 5. Karar Destek Notu

Bu rapor, satış performansının genel olarak güçlü göründüğünü fakat karar almadan önce veri kalitesi kontrolünün zorunlu olduğunu gösteriyor. Yönetici için en doğru yaklaşım; önce hatalı/eksik kayıtları düzeltmek, ardından yüksek öncelikli riskli müşterileri kontrol etmek, geciken ödemeleri takip etmek ve sonrasında satış performansını yeniden değerlendirmektir.
