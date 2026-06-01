# Proje Geçmişi — AI Virtual Data Analyst

Bu dosya v1 → v14 boyunca yapılan tüm sürüm notlarının arşividir. Güncel kullanım için [README.md](README.md)'ye bak; proje vizyonu ve çalışma kuralları için [CLAUDE.md](CLAUDE.md)'ye bak.

---

Bu proje, BI/data ekibi olmayan küçük ve orta ölçekli şirketler için geliştirilen **AI destekli sanal veri analisti** fikrinin ilk teknik demosudur.

Ürünün temel vaadi:

> Excel’den 5 dakikada yönetici raporu.

Kullanıcı bir Excel/CSV dosyası yükler. Sistem satış verisini analiz eder, veri hatalarını bulur, riskli müşterileri çıkarır ve yöneticiye okunabilir bir rapor üretir.

---

## Problem

KOBİ ve küçük ekiplerde raporlar hâlâ çoğunlukla Excel üzerinden manuel hazırlanıyor.

Bu durum üç ana probleme yol açıyor:

1. Manuel Excel raporları çok zaman alıyor.
2. Eksik, hatalı veya tutarsız veriler geç fark ediliyor.
3. Yöneticiler teknik tablo değil, sade özet ve aksiyon istiyor.

---

## Çözüm

Bu demo, satış verisi içeren bir Excel dosyasını okuyarak otomatik analiz yapar.

Sistem şu çıktıları üretir:

- Toplam satış tutarı
- Kazanılan satış toplamı
- Beklemede ve kaybedilen satış sayısı
- Veri kalitesi problemleri
- Riskli müşteri listesi
- Bölge bazlı satış özeti
- Ürün bazlı satış özeti
- Satış temsilcisi bazlı satış özeti
- Yönetici raporu

---

## Proje Yapısı

```text
ai-virtual-data-analyst-demo/
│
├── data/
│   └── Sales Demo Data.xlsx
│
├── output/
│   ├── generated_report_v2.md
│   ├── data_quality_issues.csv
│   └── risky_customers.csv
│
├── analyze_sales.py
└── README.md

 Kullanılan Teknolojiler
Python
pandas
openpyxl
Excel dosya analizi
Markdown rapor çıktısı
CSV veri kalite ve risk çıktıları
Kurulum

Gerekli paketleri yüklemek için:
pip install pandas openpyxl

Eğer openpyxl versiyon hatası alınırsa:

python -m pip install --upgrade openpyxl
Çalıştırma

Proje klasöründe terminali aç:

python analyze_sales.py

Başarılı çalışırsa terminalde şu çıktılar görünür:

Analiz tamamlandı.
Markdown rapor oluşturuldu: output/generated_report_v2.md
Veri kalite sorunları oluşturuldu: output/data_quality_issues.csv
Riskli müşteriler oluşturuldu: output/risky_customers.csv
Oluşan Çıktılar
1. generated_report_v2.md

Ana yönetici raporudur.

İçerik:

Yönetici özeti
En önemli 5 bulgu
Veri kalitesi özeti
Detaylı veri hataları
Riskli müşteriler
Aksiyon önerileri
Bölge bazlı satış özeti
Ürün bazlı satış özeti
Satış temsilcisi bazlı satış özeti
2. data_quality_issues.csv

Veri kalitesi problemlerini listeler.

Örnek problemler:

Eksik satış tutarı
Eksik bölge
Eksik satış temsilcisi
Hatalı tarih
Negatif satış tutarı
Standart dışı durum değeri
Durum/ödeme tutarsızlığı
Anormal yüksek satış
3. risky_customers.csv

Riskli müşterileri ve önerilen aksiyonları listeler.

Örnek riskler:

Geciken ödeme
Eksik satış tutarı
Negatif satış tutarı
Hatalı tarih
Durum/ödeme tutarsızlığı
Anormal yüksek satış
MVP Kapsamı

Bu demo, ilk MVP’nin teknik çekirdeğidir.

İlk MVP senaryosu:

Satış Excel’i → AI Yönetici Raporu

Mevcut demo şu işleri yapar:

Excel dosyasını okur.
Satış verisini analiz eder.
Veri hatalarını tespit eder.
Riskli müşterileri çıkarır.
Markdown formatında yönetici raporu üretir.
CSV formatında veri hatası ve risk listesi üretir.
Ürün Vizyonu

Bu demo ileride şu ürüne dönüşecektir:

BI ekibi olmayan şirketler için AI destekli sanal veri analisti.

Gelecek özellikler:

Web arayüzünden Excel/CSV yükleme
AI destekli yönetici yorumu
PDF rapor çıktısı
Dashboard görünümü
Farklı rapor türleri: satış, finans, operasyon
Kullanıcıya özel rapor şablonları
Raporla sohbet etme özelliği
Ürün Mantığı

Bu projede temel yaklaşım:

Python hesaplar, AI yorumlar.

Python tarafı kesin hesaplamaları yapar:

Toplam satış
Eksik veri
Negatif tutar
Hatalı tarih
Anomali
Riskli müşteri

AI tarafı ileride bu teknik çıktıları yönetici diline çevirecektir:

Daha doğal özet
Daha iyi aksiyon önerileri
Karar destek yorumu
Profesyonel rapor dili
Mevcut Durum

Versiyon: v2

Tamamlananlar:

Problem ve hedef müşteri netleştirildi.
Demo satış datası oluşturuldu.
Python analiz scripti yazıldı.
Markdown rapor çıktısı üretildi.
Veri kalitesi sorunları CSV olarak çıkarıldı.
Riskli müşteriler CSV olarak çıkarıldı.


## Mevcut Durum

Versiyon: v3

Tamamlananlar:

- Problem ve hedef müşteri netleştirildi.
- Demo satış datası oluşturuldu.
- Python analiz scripti yazıldı.
- Markdown rapor çıktısı üretildi.
- Veri kalitesi sorunları CSV olarak çıkarıldı.
- Riskli müşteriler CSV olarak çıkarıldı.
- Aynı müşteriye ait birden fazla risk tek satırda birleştirildi.
- PDF yönetici raporu çıktısı üretildi.

Son oluşan çıktılar:

- output/generated_report_v3.md
- output/generated_report_v3.pdf
- output/data_quality_issues.csv
- output/risky_customers.csv

Sıradaki teknik hedef:

- Analiz sonucunu JSON formatında üretmek.
- Bu JSON çıktısını ileride AI yorum katmanına ve web arayüzüne bağlamak.


## Mevcut Durum

Versiyon: v4

Tamamlananlar:

- Problem ve hedef müşteri netleştirildi.
- Demo satış datası oluşturuldu.
- Python analiz scripti yazıldı.
- Markdown rapor çıktısı üretildi.
- PDF yönetici raporu çıktısı üretildi.
- Veri kalitesi sorunları CSV olarak çıkarıldı.
- Riskli müşteriler CSV olarak çıkarıldı.
- Aynı müşteriye ait birden fazla risk tek satırda birleştirildi.
- `nan` değerleri kullanıcı dostu şekilde `Eksik değer` olarak gösterildi.
- Risk aksiyonları daha okunabilir hale getirildi.
- Web arayüzü ve AI yorum katmanı için `analysis_result_v4.json` üretildi.

Son oluşan çıktılar:

- output/generated_report_v4.md
- output/generated_report_v4.pdf
- output/analysis_result_v4.json
- output/data_quality_issues.csv
- output/risky_customers.csv

Sıradaki teknik hedef:

- v5 kapsamında AI yorum katmanı eklenecek.
- Python tarafından üretilen `analysis_result_v4.json`, AI tarafından daha doğal ve profesyonel bir yönetici yorumuna dönüştürülecek.


## v5 — AI Yorum Katmanı

v5 kapsamında Python analiz motorunun ürettiği `analysis_result_v4.json` dosyası kullanılarak yöneticiye uygun AI yorum katmanı oluşturulmuştur.

Tamamlananlar:

- `ai_prompt_v5.txt` üretildi.
- `generated_ai_summary_v5.md` üretildi.
- `generated_report_v5.md` üretildi.
- AI yorumu; yönetici özeti, ana riskler, satış performansı yorumu, öncelikli aksiyon planı ve karar destek notu bölümlerinden oluşacak şekilde tasarlandı.
- v5 çıktısı, teknik raporu doğrudan yöneticinin anlayacağı sade karar destek formatına dönüştürmeye başladı.

Not:

- Bu versiyonda gerçek AI API entegrasyonu yapılmamıştır.
- AI prompt dosyası hazırlandığı için bir sonraki adımda OpenAI API bağlantısı eklenebilir.


## v5.1 — OpenAI API Entegrasyonu Durumu

v5.1 kapsamında gerçek OpenAI API entegrasyonu denenmiştir. API anahtarı `.env` dosyasından okunmuş ve istek başarıyla gönderilmiştir.

Ancak OpenAI API hesabında aktif kredi/billing olmadığı için istek `insufficient_quota` hatasıyla durmuştur.

Bu nedenle gerçek API entegrasyonu şimdilik beklemeye alınmıştır.

Karar:

- API maliyeti oluşmaması için proje local v5 yapısıyla devam edecektir.
- `generated_ai_summary_v5.md` ve `generated_report_v5.md` mevcut demo için yeterlidir.
- Gerçek API entegrasyonu, müşteri doğrulaması veya demo ihtiyacı oluştuğunda tekrar aktive edilecektir.


## v6.1 — Streamlit Web MVP

v6.1 kapsamında proje terminal tabanlı demo olmaktan çıkarılıp Streamlit ile çalışan local web MVP haline getirilmiştir.

Tamamlananlar:

- Streamlit arayüzü oluşturuldu.
- Excel yükleme alanı eklendi.
- Analiz Et butonu eklendi.
- Python analiz motoru web arayüzünden çalıştırıldı.
- AI yönetici yorumu web ekranında gösterildi.
- Teknik rapor web ekranında gösterildi.
- Veri kalite sorunları tablo olarak gösterildi.
- Riskli müşteriler tablo olarak gösterildi.
- PDF, Markdown, JSON ve CSV indirme butonları eklendi.
- KPI kartları eklendi:
  - Toplam satış
  - Kazanılan satış
  - Veri kalite problemi
  - Riskli müşteri sayısı

Durum:

- Local çalışan, gösterilebilir ilk web MVP başarıyla ayağa kaldırıldı.
- OpenAI API entegrasyonu ödeme/billing nedeniyle beklemeye alınmıştır.
- Demo şu an local v5 AI yorum katmanı ile çalışmaktadır.


## v7 — Excel Şablon Doğrulama ve Güvenli Dosya Yükleme

v7 kapsamında Streamlit web arayüzüne Excel şablon kontrolü ve güvenli dosya yükleme akışı eklenmiştir.

Tamamlananlar:

- Örnek Excel şablonu indirme butonu eklendi.
- Yüklenen Excel dosyasının kolonları kontrol edildi.
- Eksik kolon varsa kullanıcıya anlaşılır hata mesajı gösterildi.
- Doğru formatta dosya yüklenirse dosya kaydedildi.
- Yüklenen dosyanın ilk satırları önizleme olarak gösterildi.
- Analiz öncesi mevcut Excel dosyasının kolonları tekrar kontrol edildi.
- Boş veri kalite CSV dosyası uygulamayı bozmayacak hale getirildi.
- Boş riskli müşteri CSV dosyası uygulamayı bozmayacak hale getirildi.
- Veri kalite sorunu yoksa “Veri kalite sorunu bulunamadı” mesajı gösterildi.
- Riskli müşteri yoksa “Riskli müşteri bulunamadı” mesajı gösterildi.

Durum:

- Uygulama artık farklı Excel dosyalarıyla daha güvenli çalışabilir hale geldi.
- MVP, terminal tabanlı demo olmaktan çıkıp kullanıcı etkileşimli local web ürünü seviyesine geldi.


---

## v8.1 — Kullanıcı Dostu İndirme Deneyimi

v8.1 kapsamında rapor indirme deneyimi daha ürün odaklı hale getirilmiştir.

Önceden kullanıcı teknik dosya isimleriyle karşılaşıyordu:

- `generated_report_v4.pdf`
- `generated_report_v5.md`
- `analysis_result_v4.json`
- `data_quality_issues.csv`
- `risky_customers.csv`

v8.1 sonrasında indirme dosyaları kullanıcı dostu isimlerle sunulmaya başlandı:

- `ai_yonetici_yorumu.md`
- `yonetici_raporu.md`
- `yonetici_raporu.pdf`
- `analiz_sonucu.json`
- `veri_kalite_sorunlari.csv`
- `riskli_musteriler.csv`

Tamamlananlar:

- İndir sekmesi daha düzenli hale getirildi.
- Dosyalar üç gruba ayrıldı:
  - Yönetici Raporları
  - Sunum / Paylaşım
  - Kontrol Dosyaları
- Teknik dosya isimleri kullanıcıdan gizlendi.
- İndirilen dosyalar daha temiz ve paylaşılabilir isimlerle sunuldu.

Durum:

- Uygulama artık demo/sunum sırasında daha profesyonel görünüyor.
- Kullanıcı teknik çıktı isimleriyle değil, anlamlı rapor dosyalarıyla karşılaşıyor.

---

## v9 — Kod Mimarisini Toparlama

v9 kapsamında çalışan MVP’nin kod yapısı büyümeye daha uygun hale getirilmeye başlanmıştır.

Amaç:

- Terminal scriptlerini import edilebilir fonksiyonlara dönüştürmek.
- Streamlit uygulamasını subprocess kullanımından kurtarmak.
- Kod sorumluluklarını dosya dosya ayırmak.
- Uygulamayı ileride FastAPI, React veya SaaS yapısına taşımaya daha uygun hale getirmek.

---

## v9.1 — `analyze_sales.py` Fonksiyonlaştırıldı

v9.1 kapsamında `analyze_sales.py` dosyası yalnızca terminalden çalışan bir script olmaktan çıkarılıp import edilebilir analiz motoruna dönüştürülmüştür.

Tamamlananlar:

- `main()` fonksiyonu `run_sales_analysis()` fonksiyonuna dönüştürüldü.
- Terminalden çalışma davranışı korunması için tekrar `main()` wrapper eklendi.
- `run_sales_analysis()` fonksiyonu analiz sonucunu `analysis_result` olarak döndürmeye başladı.
- `python analyze_sales.py` komutu hâlâ çalışır durumda bırakıldı.

Yeni kullanım:

```python
from analyze_sales import run_sales_analysis

analysis_result = run_sales_analysis()

v9.2 — generate_ai_summary.py Fonksiyonlaştırıldı

v9.2 kapsamında generate_ai_summary.py dosyası da import edilebilir hale getirildi.

Tamamlananlar:

main() fonksiyonu generate_ai_summary() fonksiyonuna dönüştürüldü.
Terminalden çalışma davranışı korunması için main() wrapper eklendi.
Fonksiyon artık üretilen dosya yollarını döndürüyor:
prompt_path
ai_summary_path
final_report_path
python generate_ai_summary.py komutu hâlâ çalışır durumda bırakıldı.

Yeni kullanım:

from generate_ai_summary import generate_ai_summary

generate_ai_summary()

Durum:

AI yorum katmanı artık terminal scripti olmanın yanında uygulama içinden çağrılabilir modül haline geldi.
v9.3 — Streamlit İçinde Direkt Fonksiyon Çağırma

v9.3 kapsamında Streamlit uygulaması, analiz ve AI yorum üretimi için subprocess kullanmak yerine doğrudan Python fonksiyonlarını çağırmaya başladı.

Önceki yapı:

Streamlit app.py
→ subprocess
→ python analyze_sales.py
→ python generate_ai_summary.py

Yeni yapı:

Streamlit app.py
→ run_sales_analysis()
→ generate_ai_summary()

Tamamlananlar:

run_sales_analysis import edildi.
generate_ai_summary import edildi.
run_function_with_logs() yardımcı fonksiyonu eklendi.
Fonksiyonların terminal çıktıları Streamlit içinde geliştirici logları olarak gösterilmeye devam etti.

Durum:

Uygulama daha hızlı, daha temiz ve büyümeye daha uygun hale geldi.
v9.4 — Eski Subprocess Yapısı Temizlendi

v9.4 kapsamında artık ihtiyaç kalmayan eski subprocess kodları kaldırıldı.

Tamamlananlar:

subprocess importu kaldırıldı.
sys importu kaldırıldı.
os importu kaldırıldı.
ANALYZE_SCRIPT değişkeni kaldırıldı.
AI_SUMMARY_SCRIPT değişkeni kaldırıldı.
run_script() fonksiyonu kaldırıldı.
Analiz ve AI yorum üretimi tamamen direkt fonksiyon çağrısına taşındı.

Güncel akış:

app.py
→ run_sales_analysis()
→ generate_ai_summary()
→ output dosyaları
→ Streamlit ekranı

Durum:

Streamlit uygulaması artık terminal komutu çalıştırmak yerine doğrudan proje modüllerini kullanıyor.
v9.5 — Excel Validasyon Kodunun Ayrılması

v9.5 kapsamında Excel şablon oluşturma ve dosya doğrulama işlemleri app.py içinden ayrılarak file_validator.py dosyasına taşındı.

Tamamlananlar:

file_validator.py oluşturuldu.
Zorunlu kolon listesi bu dosyaya taşındı.
Excel şablonu oluşturma fonksiyonu ayrıldı.
Yüklenen Excel dosyasını doğrulama fonksiyonu ayrıldı.
Mevcut Excel dosyasını analiz öncesi kontrol eden fonksiyon eklendi.
app.py daha sade hale getirildi.
Streamlit arayüzü artık validasyon işlemlerini ayrı modülden çağırıyor.

Yeni yapı:

app.py
→ Web arayüzü
→ Rapor gösterimi
→ İndirme butonları
→ Analiz ve AI yorum fonksiyonlarını çağırma

file_validator.py
→ Excel şablonu oluşturma
→ Yüklenen Excel dosyasını doğrulama
→ Mevcut Excel dosyasını analiz öncesi kontrol etme

analyze_sales.py
→ Satış analiz motoru

generate_ai_summary.py
→ AI yönetici yorumu üretimi

Durum:

Kod mimarisi büyümeye daha uygun hale getirildi.
Uygulama hâlâ aynı şekilde çalışıyor fakat dosya doğrulama sorumluluğu ayrı bir modüle taşındı.
Güncel Mevcut Durum

Versiyon: v9.5

Proje şu anda çalışan bir local web MVP seviyesindedir.

Güncel özellikler:

Streamlit web arayüzü
Excel şablonu indirme
Excel dosyası yükleme
Excel kolon doğrulama
Yüklenen dosya önizleme
Satış analiz motoru
Veri kalite kontrolü
Riskli müşteri analizi
KPI kartları
AI yönetici yorumu
Teknik analiz raporu
PDF rapor çıktısı
Markdown rapor çıktısı
CSV kontrol dosyaları
JSON analiz sonucu
Kullanıcı dostu indirme dosya isimleri

Güncel teknik yapı:

ai-virtual-data-analyst-demo/
│
├── app.py
├── analyze_sales.py
├── generate_ai_summary.py
├── generate_ai_summary_api.py
├── file_validator.py
├── README.md
│
├── data/
│   └── Sales Demo Data.xlsx
│
└── output/
    ├── analysis_result_v4.json
    ├── ai_prompt_v5.txt
    ├── generated_ai_summary_v5.md
    ├── generated_report_v4.md
    ├── generated_report_v4.pdf
    ├── generated_report_v5.md
    ├── data_quality_issues.csv
    └── risky_customers.csv

Sıradaki hedefler:

v9.6 kapsamında app.py içindeki yardımcı okuma/indirme fonksiyonlarını app_utils.py dosyasına taşımak.
v10 kapsamında mock datadan çıkış için daha gerçekçi test Excel dosyaları oluşturmak.
v11 kapsamında farklı Excel kolon isimlerini desteklemek için kolon eşleştirme ekranı geliştirmek.


## v9.6 — App Yardımcı Fonksiyonlarının Ayrılması

v9.6 kapsamında `app.py` içindeki genel yardımcı fonksiyonlar `app_utils.py` dosyasına taşındı.

Tamamlananlar:

- `app_utils.py` oluşturuldu.
- Dosya okuma fonksiyonları ayrıldı.
- JSON okuma fonksiyonu ayrıldı.
- CSV güvenli okuma fonksiyonu ayrıldı.
- AI summary temizleme fonksiyonu ayrıldı.
- Fonksiyon loglarını yakalayan yardımcı yapı ayrıldı.
- Download button yardımcı fonksiyonu ayrıldı.
- `app.py` daha sade ve okunabilir hale getirildi.

Durum:A

- `app.py` artık daha çok web arayüzü sorumluluğuna odaklanıyor.
- Yardımcı işlemler ayrı modüle taşındı.

---

## v10.1 — Gerçekçi Test Datalarının Üretilmesi

v10.1 kapsamında MVP'nin yalnızca küçük demo verisiyle değil, daha gerçekçi senaryolarla da test edilebilmesi için yeni test Excel dosyaları oluşturuldu.

Tamamlananlar:

- `generate_test_data.py` ile test datası üretimi eklendi.
- Temiz satış verisi oluşturuldu: `clean_sales_data.xlsx`.
- Bilinçli veri hataları içeren kirli satış verisi oluşturuldu: `dirty_sales_data.xlsx`.
- Daha büyük hacimli satış verisi oluşturuldu: `large_sales_data.xlsx`.
- Test verileri `test_data/` klasörü altında toplandı.

Durum:

- MVP artık yalnızca küçük örnek dosyayla değil, farklı kalite seviyelerindeki sentetik Excel dosyalarıyla test edilebilir hale geldi.
- Gerçek müşteri verisi kullanılmadan ürün davranışı daha güvenli şekilde doğrulanabiliyor.

---

## v10.2 — Large Data Testi

v10.2 kapsamında sistem yaklaşık 500 satırlık büyük satış datası ile test edildi.

Test sonucu:

- Toplam satış: `67.700.256 TL`
- Kazanılan satış toplamı: `22.744.126 TL`
- Veri kalite problemi: `8`
- Riskli müşteri kaydı: `21`
- Beklemede satış sayısı: `163`
- Kaybedilen satış sayısı: `175`
- En güçlü bölge: `Antalya`
- En güçlü ürün: `Paket C`
- En güçlü satış temsilcisi: `Burak`

Durum:

- Sistem büyük veri dosyasını başarıyla okuyup analiz etti.
- KPI kartları, teknik rapor, veri kalite tablosu, riskli müşteri tablosu ve AI yönetici yorumu büyük veriyle çalıştı.
- Bu test, MVP'nin küçük demo seviyesinden çıkıp daha gerçekçi dosyalarda da çalışabildiğini gösterdi.

---

## v10.3 — Risk Skoru, Öncelik ve AI Summary Düzeltmesi

v10.3 kapsamında riskli müşteri analizi daha karar odaklı hale getirildi.

Tamamlananlar:

- Riskli müşterilere `Risk Skoru` kolonu eklendi.
- Riskli müşterilere `Öncelik` kolonu eklendi.
- Riskler ağırlıklarına göre skorlandı:
  - Anormal yüksek satış: 5
  - Negatif satış tutarı: 5
  - Durum/ödeme tutarsızlığı: 4
  - Eksik satış tutarı: 4
  - Hatalı tarih: 3
  - Geciken ödeme: 2
- Riskli müşteriler risk skoruna göre büyükten küçüğe sıralanmaya başladı.
- Aynı müşteriye ait birden fazla risk tek satırda birleştirilmeye devam etti.
- `generate_ai_summary.py` risk skoru ve öncelik alanlarını dikkate alacak şekilde güncellendi.
- Eski hardcoded `Atlas Holding` yorumu kaldırıldı.
- AI Yönetici Yorumu artık JSON içindeki gerçek anormal yüksek satış müşterisini kullanıyor.

Large data final test sonucu:

- En yüksek riskli müşteri: `Nova Teknoloji`
- Risk tipi: `Geciken ödeme + Durum/ödeme tutarsızlığı + Anormal yüksek satış`
- Risk skoru: `11`
- Öncelik: `Yüksek`

Doğrulanan çıktı:

```text
Nova Teknoloji (Yüksek, skor: 11): Geciken ödeme + Durum/ödeme tutarsızlığı + Anormal yüksek satış
```

AI yorum içinde artık doğru şekilde şu mantık kullanılmaktadır:

```text
Ancak Nova Teknoloji gibi anormal yüksek satış içeren kayıtlar toplam performansı şişiriyor olabilir.
```

Durum:

- v10.3 başarıyla kapatıldı.
- Analiz motoru ve AI-like summary katmanı risk skoru / öncelik mantığıyla uyumlu çalışıyor.
- Streamlit ekranında AI Yönetici Yorumu doğru müşteri ve doğru risk skoru ile görüntüleniyor.

---

## Güncel Mevcut Durum

Versiyon: `v10.3 tamamlandı`

Proje şu anda çalışan bir local Streamlit web MVP seviyesindedir.

Güncel özellikler:

- Streamlit web arayüzü
- Excel şablonu indirme
- Excel dosyası yükleme
- Excel kolon doğrulama
- Yüklenen dosya önizleme
- Satış analiz motoru
- Veri kalite kontrolü
- Riskli müşteri analizi
- Risk skoru hesaplama
- Risk önceliklendirme
- KPI kartları
- AI-like yönetici yorumu
- Teknik analiz raporu
- PDF rapor çıktısı
- Markdown rapor çıktısı
- CSV kontrol dosyaları
- JSON analiz sonucu
- Kullanıcı dostu indirme dosya isimleri

Güncel teknik yapı:

```text
ai-virtual-data-analyst-demo/
│
├── app.py                         # Streamlit web arayüzü
├── app_utils.py                   # Dosya okuma, CSV güvenli okuma, download/log yardımcıları
├── file_validator.py              # Excel şablon ve validasyon işleri
├── analyze_sales.py               # Satış analiz motoru + risk skoru / öncelik
├── generate_ai_summary.py         # Local AI-like yönetici yorumu
├── generate_ai_summary_api.py     # OpenAI API entegrasyon denemesi (billing bekliyor)
├── generate_test_data.py          # Temiz/kirli/büyük test datası üretimi
├── README.md
│
├── data/
│   └── Sales Demo Data.xlsx
│
├── output/
│   ├── analysis_result_v4.json
│   ├── ai_prompt_v5.txt
│   ├── generated_ai_summary_v5.md
│   ├── generated_report_v4.md
│   ├── generated_report_v4.pdf
│   ├── generated_report_v5.md
│   ├── data_quality_issues.csv
│   └── risky_customers.csv
│
└── test_data/
    ├── clean_sales_data.xlsx
    ├── dirty_sales_data.xlsx
    └── large_sales_data.xlsx
```

---

## Sıradaki Hedefler

### v10.4 — Riskli Müşteriler UI İyileştirmesi

Riskli Müşteriler tabında uzun aksiyon metinleri daha okunabilir hale getirilecek.

Planlananlar:

- Risk tablosunda kısa `Aksiyon Özeti` gösterimi eklenecek.
- Uzun `Önerilen Aksiyon` metinleri isterse detay bölümünde gösterilecek.
- Tablo daha demo/pilot sunumuna uygun hale getirilecek.

### v11 — Kolon Eşleştirme Ekranı

Kullanıcının farklı Excel kolon adlarını sistem alanlarıyla eşleştirebilmesi sağlanacak.

Örnek:

```text
Sistemdeki Alan      Excel'deki Kolon
Müşteri        →     Cari Adı
Tarih          →     Fatura Tarihi
Satış Tutarı   →     Net Ciro
Bölge          →     Şehir
```

### v12 — Farklı Excel Formatlarını Destekleme

Cari Adı, Fatura Tarihi, Net Ciro, Tahsilat Durumu gibi farklı kolon isimleri desteklenecek.

### v13 — Profesyonel PDF Tasarımı

PDF raporu daha kurumsal hale getirilecek.

Planlananlar:

- Kapak alanı
- Özet KPI kartları
- Daha okunabilir tablo düzeni
- Logo alanı
- Daha temiz yönetici raporu formatı

### v14 — Deploy

Streamlit Cloud, Render veya benzeri bir platformda paylaşılabilir demo hazırlanacak.

### v15 — Gerçek AI API Entegrasyonu

OpenAI API entegrasyonu billing/quota hazır olduğunda tekrar aktive edilecek.

---

## Güvenlik Notu

Gerçek müşteri verisi kullanılmadan önce KVKK, veri gizliliği ve anonimleştirme konuları ayrıca değerlendirilmelidir.

Ayrıca `.env` dosyası, API key ve output içindeki hassas dosyalar GitHub'a gönderilmemelidir.

Mevcut karar:

- Gerçek OpenAI API entegrasyonu şimdilik beklemede.
- Local AI-like summary ile MVP geliştirmeye devam edilecek.
- Öncelik ürün doğrulaması, pilot feedback ve çalışan demo kalitesidir.



---

## v10.1 — Gerçekçi Test Datalarının Üretilmesi

v10.1 kapsamında MVP’nin yalnızca küçük demo verisiyle değil, daha gerçekçi satış dosyalarıyla da test edilebilmesi için yeni test Excel dosyaları üretildi.

Tamamlananlar:

- `generate_test_data.py` oluşturuldu.
- Temiz test datası üretildi.
- Kirli / hatalı test datası üretildi.
- Büyük hacimli test datası üretildi.
- `test_data/` klasörü altında örnek Excel dosyaları oluşturuldu:
  - `clean_sales_data.xlsx`
  - `dirty_sales_data.xlsx`
  - `large_sales_data.xlsx`

Durum:

- MVP artık farklı veri kalitesi seviyelerine sahip dosyalarla test edilebilir hale geldi.

---

## v10.2 — Large Data Testi

v10.2 kapsamında sistem yaklaşık 500 satırlık büyük satış datası ile test edildi.

Test sonucu:

- Toplam satış: `67.700.256 TL`
- Kazanılan satış toplamı: `22.744.126 TL`
- Veri kalite problemi: `8`
- Riskli müşteri kaydı: `21`
- Beklemede satış sayısı: `163`
- Kaybedilen satış sayısı: `175`
- En güçlü bölge: `Antalya`
- En güçlü ürün: `Paket C`
- En güçlü satış temsilcisi: `Burak`

Durum:

- Analiz motoru büyük test datasını başarıyla okuyabildi.
- KPI, veri kalite sorunları, riskli müşteriler ve teknik rapor çıktıları doğru üretildi.
- MVP küçük demo dosyasından çıkarak daha gerçekçi veriyle test edilmiş oldu.

---

## v10.3 — Risk Skoru, Öncelik ve AI Summary Düzeltmesi

v10.3 kapsamında riskli müşteriler sadece listelenmek yerine risk ağırlığına göre skorlanmaya ve önceliklendirilmeye başlandı.

Tamamlananlar:

- Riskli müşterilere `Risk Skoru` kolonu eklendi.
- Riskli müşterilere `Öncelik` kolonu eklendi.
- Risk skoru yüksek olan müşteriler tablonun üstüne alınmaya başladı.
- Risk ağırlıkları tanımlandı:
  - Anormal yüksek satış: 5
  - Negatif satış tutarı: 5
  - Durum/ödeme tutarsızlığı: 4
  - Eksik satış tutarı: 4
  - Hatalı tarih: 3
  - Geciken ödeme: 2
- Öncelik seviyeleri tanımlandı:
  - 5 ve üzeri: Yüksek
  - 3-4: Orta
  - 0-2: Düşük
- `generate_ai_summary.py` risk skorunu ve önceliği dikkate alacak şekilde güncellendi.
- Eski hardcoded `Atlas Holding` anormal yüksek satış yorumu kaldırıldı.
- AI yönetici yorumu artık gerçek riskli müşteriyi JSON’dan okuyarak yazıyor.

Son test sonucu:

- `Nova Teknoloji` risk skoru `11` ile en yüksek riskli müşteri olarak göründü.
- AI yorumunda anormal yüksek satış yorumu doğru şekilde `Nova Teknoloji` üzerinden üretildi.

Durum:

- v10.3 başarıyla kapatıldı.
- Risk skoru, önceliklendirme ve AI summary düzeltmesi çalışır durumda.

---

## v10.4 — Riskli Müşteriler UI Sadeleştirme

v10.4 kapsamında Riskli Müşteriler tabındaki uzun aksiyon metinleri sadeleştirildi.

Önceden ana tabloda uzun `Önerilen Aksiyon` metinleri yer aldığı için tablo okunması zor hale geliyordu.

Tamamlananlar:

- Riskli Müşteriler tabına `Öncelik filtresi` eklendi.
- Kullanıcı artık riskleri şu seviyelere göre filtreleyebilir:
  - Tümü
  - Yüksek
  - Orta
  - Düşük
- Ana tablo sadeleştirildi.
- Uzun `Önerilen Aksiyon` metni ana tablodan kaldırıldı.
- Bunun yerine kısa `Aksiyon Özeti` kolonu eklendi.
- Detaylı aksiyon metinleri ayrı bir expander alanında gösterilmeye başladı.
- Risk skoru ve öncelik kolonları korunmaya devam etti.

Ana tabloda gösterilen kolonlar:

- Öncelik
- Müşteri
- Risk Skoru
- Risk Tipi
- Aksiyon Özeti

Durum:

- Riskli Müşteriler ekranı daha okunabilir ve ürün gibi hale getirildi.
- v10.4 başarıyla kapatıldı.

---

## v12 — Farklı Excel Formatları Hazırlığı

v12, çoklu rapor türü vizyonunun (satış, muhasebe/tahsilat, stok, operasyon) zeminini hazırlar ve kolon eşleştirme deneyimini tekrar kullanılabilir hale getirir.

### v12.1 — Sales Schema Modülerleştirme

Sales-spesifik şema sabitleri `file_validator.py` içinden ayrı bir modüle taşındı.

Tamamlananlar:

- `report_schemas/sales.py` oluşturuldu: `REQUIRED_COLUMNS`, `COLUMN_ALIASES`, `OPTIONAL_AUTO_FILL_VALUES`, `TEMPLATE_SAMPLE_DATA`.
- `file_validator.py` artık şemayı `report_schemas.sales` üzerinden import ediyor.
- Davranış değişmedi; sadece zemin hazırlandı.
- `app.py` içindeki şema/yardımcı fonksiyon duplikasyonu kaldırıldı, tek kaynak `file_validator` oldu.

İleride `report_schemas/collections.py`, `report_schemas/inventory.py` gibi modüller eklenerek çoklu rapor türü desteklenebilir.

### v12.2 — Kolon Eşleştirme Hafızası

Kolon eşleştirme ekranında yapılan seçimler artık dosya yapısına göre kaydedilir; aynı yapıdaki Excel tekrar yüklendiğinde otomatik uygulanır.

Tamamlananlar:

- Kolon imzası (sıralı normalize edilmiş kolon adlarının SHA-256 hash'i) anahtarıyla mapping saklanır.
- `.column_mappings.json` projenin kökünde tutulur ve `.gitignore` ile takip dışı bırakılmıştır.
- Aynı yapıdaki Excel yüklendiğinde "Kayıtlı eşleştirme bulundu" bilgisi gösterilir ve seçim kutuları önceki seçimle doldurulur.
- `NO_MAPPING_LABEL` seçimi de hatırlanır.
- Farklı yapıdaki dosyada otomatik dolum yapılmaz; mevcut alias tahmini fallback olarak çalışır.

---

## v13 — Profesyonel PDF Rapor Tasarımı

Mevcut sade PDF (Markdown'ı satır satır basıyordu) yerine yapılandırılmış 6 sayfalık kurumsal bir rapor üretildi. PDF artık ham markdown'dan değil doğrudan `analysis_result` JSON'undan üretiliyor.

Yapı:

1. **Kapak Sayfası** — Başlık, marka, rapor tarihi, kaynak dosya adı, logo alanı placeholder'ı, tagline.
2. **Genel Bakış + Yönetici Özeti** — 4 KPI kartı (2x2 grid, renk kodlu), öne çıkanlar (bölge/ürün/temsilci), dinamik özet paragrafı.
3. **Riskli Müşteriler** — Risk skoruna göre sıralı tablo; Öncelik kolonu renk kodlu (Yüksek=kırmızı, Orta=turuncu, Düşük=yeşil).
4. **Veri Kalite Problemleri** — Tam tablo (Satır, Müşteri, Problem, Mevcut Değer, Aksiyon).
5. **Bölge / Ürün / Satış Temsilcisi Bazlı Satış** — Üç ayrı tablo.
6. **Öncelikli Aksiyon Planı** — Numaralı liste.

Görsel detaylar:

- Her sayfada (kapak hariç) marka header'ı + ince ayırıcı çizgi.
- Footer'da sayfa numarası.
- Tablolar gerçek tablo (başlık banner'lı, zebra striping'li).
- Tablolar sayfa sonunda taşarsa başlık otomatik tekrar eder.
- Tüm değerler `analysis_result` JSON'undan dinamik olarak gelir; hardcoded içerik yoktur.
- Arial Unicode (Windows) varsa Türkçe karakterler için kullanılır; yoksa Helvetica fallback.

Teknik:

- Yeni `ReportPDF(FPDF)` sınıfı header/footer için.
- `create_pdf_report(analysis_result, output_path)` imzası: artık dict alır, markdown listesi değil.
- Yardımcılar: `_draw_cover_page`, `_draw_kpi_cards`, `_draw_highlights`, `_draw_executive_paragraph`, `_draw_risk_table`, `_draw_data_quality_table`, `_draw_breakdown_table`, `_draw_recommendations`, `_draw_table` (genel tablo çizici).

---

## v14 — Demo Deploy Hazırlığı

Streamlit Cloud üzerinde halka açık demo deploy için proje cross-platform hale getirildi.

Tamamlananlar:

- `data/` klasörü standardize edildi (eski `Data/` → `data/`). Linux/macOS case-sensitive dosya sistemlerinde sorun çıkarmaması için.
- `requirements.txt` eklendi: `streamlit`, `pandas`, `openpyxl`, `fpdf2` minimum sürümleriyle.
- `fonts/` klasörü oluşturuldu ve `DejaVuSans.ttf` + `DejaVuSans-Bold.ttf` bundle edildi. Böylece PDF üretimi Windows-bağımsız hale geldi ve Türkçe karakterler her ortamda doğru render edilir.
- `analyze_sales.py` font yolu mantığı güncellendi: önce bundled fonta bakar, yoksa Windows fontuna düşer.
- `.streamlit/config.toml` eklendi: kurumsal light tema, 10 MB upload limit, kullanım istatistiği toplama kapalı.
- `.gitignore` genişletildi: `output/` (runtime artifact), `.env`, `.column_mappings.json`, `__pycache__/`, `*.pyc`.

### Streamlit Cloud Deploy Adımları

1. **GitHub'a push:**
   ```
   git add .
   git commit -m "v14: deploy hazırlığı"
   git push origin main
   ```

2. **Streamlit Cloud'da deploy:**
   - https://share.streamlit.io adresine git
   - "New app" → GitHub hesabını bağla
   - Repo: `ai-virtual-data-analyst-demo`
   - Branch: `main`
   - Main file: `app.py`
   - Deploy'a tıkla

3. **Public URL** — Streamlit Cloud `*.streamlit.app` formatında bir URL verecek. Bu URL müşteri demosunda ve LinkedIn'de paylaşılabilir.

### Deploy Sonrası Test Checklist

- [ ] Uygulama açılıyor
- [ ] Örnek Excel şablonu indirilebiliyor
- [ ] Yükleme + analiz çalışıyor
- [ ] PDF Türkçe karakterleri doğru render ediyor (ş, ı, ğ, ç, Ö, İ vb.)
- [ ] Kolon eşleştirme ekranı standart olmayan Excel için çıkıyor
- [ ] Tüm indirme butonları çalışıyor

### Güvenlik Notu

- `.env` deploy'a dahil edilmez (gitignored). OpenAI API entegrasyonu kapalı; deploy edilen demo local AI-like summary kullanır.
- Demo için bundled veri (`data/Sales Demo Data.xlsx`) sentetiktir. Gerçek müşteri verisi commit edilmemelidir.

---

## Güncel Mevcut Durum

Versiyon: `v14`

Proje şu anda çalışan bir local Streamlit MVP seviyesindedir.

Güncel özellikler:

- Excel şablonu indirme
- Excel dosyası yükleme
- Excel kolon doğrulama
- Dosya önizleme
- Satış analiz motoru
- Toplam satış ve kazanılan satış KPI’ları
- Bölge, ürün ve satış temsilcisi kırılımları
- Veri kalite kontrolü
- Riskli müşteri analizi
- Risk skoru ve önceliklendirme
- AI-like yönetici yorumu
- Teknik analiz raporu
- PDF, Markdown, CSV ve JSON çıktıları
- Kullanıcı dostu indirme isimleri
- Riskli müşteriler için sadeleştirilmiş UI
- Öncelik filtresi
- Kısa aksiyon özeti ve detaylı aksiyon ayrımı

Güncel teknik yapı:

```text
ai-virtual-data-analyst-demo/
│
├── app.py
├── app_utils.py
├── analyze_sales.py
├── generate_ai_summary.py
├── generate_ai_summary_api.py
├── file_validator.py
├── generate_test_data.py
├── README.md
│
├── data/
│   └── Sales Demo Data.xlsx
│
├── output/
│   ├── analysis_result_v4.json
│   ├── ai_prompt_v5.txt
│   ├── generated_ai_summary_v5.md
│   ├── generated_report_v4.md
│   ├── generated_report_v4.pdf
│   ├── generated_report_v5.md
│   ├── data_quality_issues.csv
│   └── risky_customers.csv
│
└── test_data/
    ├── clean_sales_data.xlsx
    ├── dirty_sales_data.xlsx
    └── large_sales_data.xlsx


---

## v11.1 — Kolon Eşleştirme Ekranı

v11.1 kapsamında kullanıcıların yalnızca sabit Excel şablonuyla çalışması zorunluluğu azaltıldı. Artık yüklenen Excel dosyasındaki kolon adları sistemin beklediği kolonlarla birebir aynı değilse uygulama doğrudan hata vermek yerine kolon eşleştirme ekranı gösterir.

Tamamlananlar:

- Farklı kolon isimlerine sahip Excel dosyaları için kolon eşleştirme ekranı eklendi.
- Kullanıcı sistem alanlarını kendi Excel kolonlarıyla manuel olarak eşleştirebilir hale geldi.
- Eşleştirme sonrası dosya sistemin beklediği standart formata dönüştürülüyor.
- Standart formata çevrilen dosya `data/Sales Demo Data.xlsx` olarak kaydediliyor.
- Analiz motoru değiştirilmeden mevcut analiz akışı korundu.
- Doğru şablonlu dosyalarda eski akış bozulmadan çalışmaya devam ediyor.

Örnek eşleştirme:

```text
Sistem Alanı        Kullanıcı Excel Kolonu
Tarih         →     Fatura Tarihi
Müşteri       →     Ad / Cari Adı / Firma Adı
Satış Temsilcisi →  Temsilci / Satışçı
Bölge         →     Şehir / İl
Satış Tutarı  →     Net Ciro / Tutar
```

İlgili kod: `app.py` (kolon eşleştirme ekranı, oturum durumu) ve `file_validator.py` (`get_column_mapping_defaults`, `build_mapped_dataframe`).

---

## v10.3 / v11.1 — Doğrulama Notu (2026-05-31)

Mevcut ürün durumu güvenlik ve dinamiklik açısından doğrulandı.

Doğrulanan noktalar:

- `.env` dosyası `.gitignore` içinde, git tarafından takip edilmiyor, geçmişte hiç commit edilmemiş.
- `generate_ai_summary.py` içinde hardcoded müşteri adı yok. AI yönetici yorumu, `analysis_result_v4.json` içindeki `risks.customers` listesinden Risk Skoru'na göre dinamik olarak üretiliyor. Outlier cümlesi `Anormal yüksek satış` etiketli müşterilerin gerçek adlarını kullanıyor; yoksa varmış gibi davranmıyor.
- `python -m compileall .` temiz geçiyor.
- Clean / dirty / large test dosyaları ile uçtan uca analiz + AI summary akışı başarılı.

Large data benchmark (referans için):

```text
Toplam satış: 67.700.256 TL
Kazanılan satış: 22.744.126 TL
Veri kalite problemi: 8
Riskli müşteri: 21
Top region: Antalya
Top product: Paket C
Top sales rep: Burak
Top risk customer: Nova Teknoloji (skor 11)
```

OpenAI API entegrasyonu (`generate_ai_summary_api.py`) hâlâ kapalı; local AI-like summary mevcut MVP için yeterli.

Satış Tutarı → Satış Tutarı