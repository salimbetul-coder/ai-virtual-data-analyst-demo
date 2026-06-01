# Test Rehberi — AI Virtual Data Analyst

Bu döküman v14 Streamlit MVP'sini sürüm öncesi veya demo öncesi manuel olarak test etmek içindir. Tüm test verisi sentetiktir (`test_data/`); gerçek müşteri verisi gerekmez.

## İçerik

1. [Hızlı sağlık kontrolü](#1-hızlı-sağlık-kontrolü-1-dk)
2. [Test verisi senaryoları](#2-test-verisi-senaryoları)
3. [UI test akışı](#3-ui-test-akışı)
4. [Kolon eşleştirme testi](#4-kolon-eşleştirme-testi-v111--mapping-memory-v122)
5. [PDF kalite testi](#5-pdf-kalite-testi-v13)
6. [Cloud deploy testi](#6-cloud-deploy-testi)
7. [Hata teşhisi](#7-hata-teşhisi)

---

## 1. Hızlı sağlık kontrolü (1 dk)

Komut satırından her şeyin import edilebildiğini ve uçtan uca pipeline'ın çalıştığını doğrula:

```powershell
python -m compileall .              # Syntax temizliği
python generate_test_data.py        # test_data/ altında 3 dosyayı üretir/yeniler
python analyze_sales.py             # data/Sales Demo Data.xlsx → output/ üretir
python generate_ai_summary.py       # AI yönetici yorumu + birleşik rapor
```

Hiçbir komut Python traceback'i üretmemelidir. Her komut sonunda `output/` altında dosyaların oluştuğunu doğrula.

---

## 2. Test verisi senaryoları

`test_data/` klasöründe üç farklı zorluk seviyesinde sentetik dosya vardır. Her senaryo için **beklenen metrikler aşağıda sabittir** (rastgele üretim değildir, deterministiktir).

> **Not:** Bir senaryoyu çalıştırmak için ilgili dosyayı `data/Sales Demo Data.xlsx` üzerine kopyala, sonra `python analyze_sales.py` çalıştır.
> ```powershell
> Copy-Item "test_data/large_sales_data.xlsx" "data/Sales Demo Data.xlsx"
> python analyze_sales.py
> python generate_ai_summary.py
> ```

### 2.1 `clean_sales_data.xlsx` — Temiz veri

Bu senaryo "sistem hata vermiyor, sade durumda boş tabloları nasıl gösteriyor?" sorusunu test eder.

| Metrik | Beklenen değer |
|---|---|
| Toplam satış | **6.284.262 TL** |
| Kazanılan satış | **2.703.120 TL** |
| Beklemede satış sayısı | 18 |
| Kaybedilen satış sayısı | 17 |
| Veri kalite problemi | **0** |
| Riskli müşteri kaydı | **0** |
| En güçlü bölge | İzmir |
| En güçlü ürün | Paket A |
| En güçlü temsilci | Elif |

**Doğrulanması gereken davranışlar:**
- UI "Veri Kalitesi" sekmesi boş CSV'yi düzgün gösteriyor (`Veri kalite problemi bulunamadı.` mesajı veya boş tablo)
- UI "Riskli Müşteriler" sekmesi boş CSV'yi düzgün gösteriyor (`Riskli müşteri bulunamadı.` mesajı)
- AI Yönetici Yorumu outlier cümlesinde hayalî müşteri uydurmuyor (CLAUDE.md kuralı)
- PDF altıncı sayfaya kadar oluşuyor (boş tablolarla bile crash etmiyor)

### 2.2 `dirty_sales_data.xlsx` — Sorunlu veri

Bu senaryo "sistem bilinen 8 anomali tipini yakalıyor mu?" sorusunu test eder.

| Metrik | Beklenen değer |
|---|---|
| Toplam satış | **1.236.000 TL** |
| Kazanılan satış | **1.004.000 TL** |
| Beklemede satış sayısı | 3 |
| Kaybedilen satış sayısı | 1 |
| Veri kalite problemi | **8** |
| Riskli müşteri kaydı | **6** |
| En güçlü bölge | İstanbul |
| En güçlü ürün | Paket C |
| En güçlü temsilci | Ayşe |
| En yüksek risk müşterisi | Atlas Holding (skor 5, Yüksek) |

**Doğrulanması gereken 8 veri kalite problemi:**
- Eksik satış tutarı
- Eksik bölge
- Eksik satış temsilcisi
- Hatalı tarih (örn. `2026-14-20` ay > 12)
- Negatif satış tutarı
- Standart dışı durum değeri (örn. `Tamamlandı`)
- Durum/ödeme tutarsızlığı (örn. `Kaybedildi` + `Ödendi`)
- Anormal yüksek satış (outlier)

### 2.3 `large_sales_data.xlsx` — 500 satırlık demo veri

Bu senaryo gerçekçi hacimde performans ve müşteri demosu için kullanılır. Tüm benchmark sayıları sabittir.

| Metrik | Beklenen değer |
|---|---|
| Toplam satış | **67.700.256 TL** |
| Kazanılan satış | **22.744.126 TL** |
| Beklemede satış sayısı | 163 |
| Kaybedilen satış sayısı | 175 |
| Veri kalite problemi | **8** |
| Riskli müşteri kaydı | **21** |
| En güçlü bölge | Antalya |
| En güçlü ürün | Paket C |
| En güçlü temsilci | Burak |
| En yüksek risk müşterisi | **Nova Teknoloji** (skor **11**, Yüksek) |

**Doğrulanması gereken davranışlar:**
- AI Yönetici Yorumu bölüm 2'de "**Nova Teknoloji** (Yüksek, skor: 11)" yazıyor (hardcoded değil — JSON'dan dinamik gelir)
- AI Yönetici Yorumu bölüm 3 outlier cümlesi "Nova Teknoloji gibi anormal yüksek satış..." diyor
- PDF risk tablosu Risk Skoru'na göre sıralı; ilk satır Nova Teknoloji
- KPI kartları, breakdown tabloları ve aksiyon planı 5 saniye altında üretiliyor

---

## 3. UI test akışı

`streamlit run app.py` ile lokal başlat veya cloud demoya git: https://ai-virtual-data-analyst.streamlit.app

### Standart akış (3 dk)

1. **"Örnek Excel Şablonunu İndir"** butonuna bas → şablon iniyor mu?
2. **"Satış Excel dosyanı yükle"** → `test_data/large_sales_data.xlsx`'i seç
3. Yeşil "Dosya doğrulandı..." mesajı çıkmalı
4. **"Analiz Et"** kırmızı butonuna bas
5. Sekmelerin yüklenmesini bekle (~5 sn)

**Sekme sekme kontrol et:**

| Sekme | Doğrulama |
|---|---|
| Genel Durum (üst) | 4 KPI kartı: 67.700.256 TL · 22.744.126 TL · 8 · 21 |
| Genel Durum altı | "En güçlü bölge: Antalya" / ürün: Paket C / temsilci: Burak |
| AI Yönetici Yorumu | Bölüm 2'de Nova Teknoloji skor 11; bölüm 3'te outlier Nova Teknoloji |
| Teknik Rapor | 9 bölümlük Markdown, tablolar düzgün |
| Veri Kalitesi | 8 satırlı tablo, hepsi açıklama içeriyor |
| Riskli Müşteriler | Öncelik filtresi (Tümü/Yüksek/Düşük) çalışıyor; "Aksiyon Özeti" kısa cümleler; expander uzun aksiyonları gösteriyor |
| İndir | 6 buton (AI yorum, birleşik, PDF, JSON, veri kalite CSV, riskli CSV) hepsi indirebiliyor |

---

## 4. Kolon eşleştirme testi (v11.1 + mapping memory v12.2)

Bu test sistemin standart olmayan Excel formatlarını desteklediğini ve aynı yapıyı bir kez eşleştirdiğinde hatırladığını doğrular.

### Hazırlık

1. **"Örnek Excel Şablonunu İndir"** butonuyla şablonu indir
2. İndirilen `template.xlsx` (veya benzeri ad) dosyasını Excel/LibreOffice'te aç
3. Aşağıdaki kolon adlarını değiştir:
   - `Müşteri` → `Cari Adı`
   - `Satış Tutarı` → `Net Ciro`
   - `Tarih` → `Fatura Tarihi`
   - `Bölge` → `Şehir`
   - `Satış Temsilcisi` → `Satışçı`
4. **Farklı bir isimle kaydet** (örn: `custom_columns.xlsx`)

### Test 1: Eşleştirme ekranı çıkıyor mu

1. Streamlit uygulamasına `custom_columns.xlsx`'i yükle
2. **Beklenen:** sarı uyarı + "Kolon Eşleştirme" bölümü açılır
3. Sistem otomatik öneri yapıyor mu kontrol et — `Cari Adı → Müşteri`, `Net Ciro → Satış Tutarı` vb. zaten seçili gelmeli
4. **"Kolonları Eşleştir ve Kaydet"** butonuna bas
5. **Beklenen:** yeşil "Eşleştirme kaydedildi" mesajı

### Test 2: Mapping memory hatırlıyor mu

1. Aynı `custom_columns.xlsx` dosyasını **tekrar yükle**
2. **Beklenen:** kolon eşleştirme ekranının üstünde yeşil banner: "Bu dosya yapısı için daha önce kaydedilmiş eşleştirme bulundu. Otomatik olarak yüklendi..."
3. Seçim kutuları önceki eşleştirmeyle dolu olmalı
4. (İsteğe bağlı) Test 1'deki eşleştirmeyi değiştirip kaydedersen, sonraki yüklemede yeni mapping geçerli olur

### Test 3: Farklı dosya yapısı için mapping karışmıyor

1. Farklı kolon adlarıyla başka bir Excel hazırla (örn: `Date`, `Customer`, `Amount`)
2. Yükle → **Beklenen:** mapping memory devreye girmez (çünkü kolon imzası farklı), alias-tabanlı tahmin gelir

---

## 5. PDF kalite testi (v13)

İndir sekmesinden **"PDF Yönetici Raporu"** butonuna bas → PDF'i bilgisayar görüntüleyicide aç.

| Kontrol noktası | Beklenen |
|---|---|
| Sayfa sayısı | **6 sayfa** |
| Sayfa 1 (kapak) | Sol kenarda mavi dikey şerit; "YÖNETİCİ RAPORU" küçük üst etiket; "Satış Performansı" büyük başlık; tarih + kaynak dosya + rapor türü info bloğu |
| Sayfa 2 (Genel Bakış) | Üstte mor "AI Virtual Data Analyst" header; 4 KPI kartı 2x2 grid; her kartta üstte ince renkli accent şerit; 3 highlight kart (En güçlü bölge/ürün/temsilci) |
| Sayfa 3 (Riskli Müşteriler) | "ÖNCELİK" kolonunda renkli pill badge'ler: kırmızı (YÜKSEK), turuncu (ORTA), yeşil (DÜŞÜK); risk skoruna göre sıralı |
| Sayfa 4 (Veri Kalite) | 8 satırlı tablo, her satır okunaklı |
| Sayfa 5 (Bölge + Ürün) | İki tablo yan yana değil alt alta; para tutarları **sağa yaslı** |
| Sayfa 6 (Temsilci + Aksiyon Planı) | Temsilci tablosu + numaralı aksiyon listesi; her numara mavi badge içinde |
| Türkçe karakterler | **ş, ı, ğ, ç, ü, ö, İ, Ş hepsi okunabilir** — bozuk kare, soru işareti, ya da Latin1 dönüşmüş "s/i/g/c" yok |
| Tüm sayfalar | Üstte ince hairline çizgi + sağda "Yönetici Raporu · TARİH"; altta tagline + sayfa numarası |

---

## 6. Cloud deploy testi

Streamlit Cloud canlı demosu: https://ai-virtual-data-analyst.streamlit.app

Lokal testlerinin aynısını cloud URL'inde tekrarla. Tek beklenen fark:
- Dosya upload'u internet üzerinden olduğu için 1-2 sn daha yavaş olabilir
- İlk açılışta cold start 5-10 sn sürebilir

### Cloud-spesifik doğrulamalar

- [ ] `Türkçe karakterler PDF'de doğru` (font bundling Linux'ta çalışıyor mu)
- [ ] `data/Sales Demo Data.xlsx` cloud'da mevcut (bundled veri pushlandı mı)
- [ ] Her sekme açılıyor (output dosyaları cloud'da yazılabilir mi)
- [ ] Mapping memory cloud restart sonrası kaybolur (geçici dosya sistemi) — bu beklenen davranış, v15+ SaaS'a girince persistent storage gerekir

---

## 7. Hata teşhisi

### Lokal hata
PowerShell konsolundaki traceback'i oku. Yaygın sebepler:

| Hata | Sebep | Çözüm |
|---|---|---|
| `ModuleNotFoundError: No module named X` | requirements eksik | `pip install -r requirements.txt` |
| `FileNotFoundError: Sales Demo Data.xlsx` | data klasörü boş | `python generate_test_data.py` çalıştır, sonra bir test verisini `data/` altına kopyala |
| `FPDFException: Undefined font` | Bundled font eksik | `fonts/DejaVuSans.ttf` ve `fonts/DejaVuSans-Bold.ttf` var mı kontrol et |
| `UnicodeDecodeError` | CSV encoding | Yüklenen Excel'in UTF-8 uyumlu olduğunu kontrol et |

### Cloud hata
1. https://share.streamlit.io → uygulamana git
2. Sağ alttan **"Manage app"** → Logs sekmesi
3. Son 50 satırı oku, Python traceback'i ara

---

## Otomasyon notu

Bu test rehberi şu an manuel. Otomatize pytest senaryoları **kasıtlı olarak yazılmamış** çünkü:
- MVP henüz müşteri pilotu öncesi
- UI testleri Streamlit'in test araçlarıyla yapılır (st.testing) — v16+ SaaS aşamasında eklenir
- Mevcut benchmark karşılaştırmaları snapshot testi olarak yeterli (CLAUDE.md'deki sabit değerler)

İlk müşteri pilotu öncesi `pytest` ile şunlar otomatize edilebilir:
- 3 test verisi için snapshot benchmark karşılaştırması
- `file_validator` saved-mapping round-trip
- `analyze_sales` JSON output schema doğrulaması
