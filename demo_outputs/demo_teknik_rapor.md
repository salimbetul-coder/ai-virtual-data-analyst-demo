# Mayıs 2026 Satış Yönetici Raporu

## 1. Yönetici Özeti

Ham veriye göre toplam satış tutarı **67.700.256 TL** görünmektedir.
Kazanılan satışların toplamı **22.744.126 TL** olarak hesaplanmıştır.
En yüksek satış hacmi görünen bölge **Antalya**, en güçlü ürün ise **Paket C** olarak görünmektedir.
En yüksek satış hacmine sahip satış temsilcisi **Burak** olarak hesaplanmıştır.
Ancak veri içinde kalite problemleri bulunduğu için bu rapor karar öncesi kontrol edilmelidir.

## 2. En Önemli 5 Bulgu

1. Toplam satış: **67.700.256 TL**
2. Kazanılan satış toplamı: **22.744.126 TL**
3. Beklemede olan satış sayısı: **163**
4. Kaybedilen satış sayısı: **175**
5. Riskli müşteri kaydı sayısı: **21**

## 3. Veri Kalitesi Özeti

- Toplam veri kalite problemi: **8**
- Geciken ödeme veya finansal risk kaydı: **21**

## 4. Detaylı Veri Hataları

| Satır | Müşteri | Problem | Mevcut Değer | Önerilen Aksiyon |
|---:|---|---|---|---|
| 17 | Eksen Otomotiv | Eksik satış tutarı | Eksik değer | Satış tutarı tamamlanmalı. |
| 44 | Kare Mobilya | Eksik bölge | Eksik değer | Bölge bilgisi tamamlanmalı. |
| 80 | Nova Teknoloji | Eksik satış temsilcisi | Eksik değer | Satış temsilcisi bilgisi tamamlanmalı. |
| 122 | Star Medya | Hatalı tarih | 2026-14-20 | Tarih formatı kontrol edilmeli. |
| 157 | Mira Perakende | Negatif satış tutarı | -25.000 | Bu kayıt iade mi yoksa veri hatası mı kontrol edilmeli. |
| 212 | Delta İnşaat | Standart dışı durum değeri | Tamamlandı | Durum alanı Kazanıldı, Beklemede veya Kaybedildi değerlerinden biri olmalı. |
| 262 | Nova Teknoloji | Durum/ödeme tutarsızlığı | Durum=Kaybedildi, Ödeme Durumu=Ödendi | Satış kaydı ve ödeme durumu birlikte doğrulanmalı. |
| 322 | Nova Teknoloji | Anormal yüksek satış | 1.500.000 | Bu satış gerçek mi yoksa veri girişi hatası mı kontrol edilmeli. |

## 5. Riskli Müşteriler

| Öncelik | Müşteri | Risk Tipi | Risk Skoru | Önerilen Aksiyon |
|---|---|---|---:|---|
| Yüksek | Nova Teknoloji | Geciken ödeme + Durum/ödeme tutarsızlığı + Anormal yüksek satış | 11 | Tahsilat takip listesine alınmalı; kayıt satış veya finans ekibi tarafından kontrol edilmeli; gerçek satışsa stratejik müşteri olarak takip edilmeli; hataysa düzeltilmeli. |
| Yüksek | Mira Perakende | Geciken ödeme + Negatif satış tutarı | 7 | Tahsilat takip listesine alınmalı; finans/muhasebe ekibi bu kaydı doğrulamalı. |
| Yüksek | Eksen Otomotiv | Eksik satış tutarı + Geciken ödeme | 6 | Tutar bilgisi tamamlanmadan rapor hesaplamasına güvenilmemeli; tahsilat takip listesine alınmalı. |
| Yüksek | Star Medya | Geciken ödeme + Hatalı tarih | 5 | Tahsilat takip listesine alınmalı; tarih düzeltilmeden dönemsel analiz yapılmamalı. |
| Düşük | Akdeniz Turizm | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | Atlas Holding | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | Bora Enerji | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | Delta İnşaat | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | Ege Kozmetik | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | Kare Mobilya | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | Kuzey Market | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | Lima Gıda | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | Mavi Lojistik | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | Mega Grup | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | Orion Yazılım | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | Pera Tekstil | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | Rota Eğitim | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | Safir Medikal | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | Vera Danışmanlık | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | Zen Yapı | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |
| Düşük | İnci Sağlık | Geciken ödeme | 2 | Tahsilat takip listesine alınmalı. |

## 6. Aksiyon Önerileri

1. Eksik, negatif ve hatalı tarih içeren kayıtlar düzeltilmeden nihai rapor kullanılmamalı.
2. Geciken ödemeler için tahsilat takip listesi oluşturulmalı.
3. Anormal yüksek satışlar gerçek mi veri hatası mı kontrol edilmeli.
4. Beklemede olan satışlar için satış temsilcileri hızlı takip yapmalı.
5. Durum alanı Kazanıldı, Beklemede, Kaybedildi değerleriyle standartlaştırılmalı.

## 7. Bölge Bazlı Satış Özeti

| Bölge | Satış Tutarı |
|---|---:|
| Antalya | 14.420.409 TL |
| Ankara | 11.777.147 TL |
| İstanbul | 11.311.584 TL |
| Bursa | 10.311.814 TL |
| İzmir | 10.139.884 TL |
| Konya | 9.681.895 TL |
| Bölge eksik | 57.523 TL |

## 8. Ürün Bazlı Satış Özeti

| Ürün | Satış Tutarı |
|---|---:|
| Paket C | 26.129.817 TL |
| Paket B | 21.895.718 TL |
| Paket A | 19.674.721 TL |

## 9. Satış Temsilcisi Bazlı Satış Özeti

| Satış Temsilcisi | Satış Tutarı |
|---|---:|
| Burak | 12.540.179 TL |
| Ayşe | 12.006.864 TL |
| Zeynep | 11.839.642 TL |
| Can | 11.701.238 TL |
| Elif | 10.631.415 TL |
| Mehmet | 8.951.483 TL |
| Satış temsilcisi eksik | 29.435 TL |