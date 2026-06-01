# CLAUDE CODE PROJECT CONTEXT

# AI Virtual Data Team — Proje Hafızası, Teknik Bağlam ve Çalışma Talimatı

Bu belge Claude Code'un projeyi sıfırdan anlayıp güvenli şekilde geliştirmeye devam edebilmesi için hazırlanmıştır. Belgeyi proje kök dizinine `CLAUDE.md` olarak koymak en doğru kullanım şeklidir. Claude Code her çalışma başında bu dosyayı okumalı, mevcut dosyaları incelemeli ve değişiklikleri küçük, test edilebilir adımlarla yapmalıdır.

---

## 0. En kısa özet

Proje artık sadece `AI Virtual Data Analyst` değildir. Yeni ana vizyon:

> **AI Virtual Data Team**: Data/BI ekibi olmayan şirketler için AI destekli sanal veri ekibi.

İlk çalışan ürün/paket:

> **AI Virtual Data Analyst**: Kullanıcı Excel yükler, sistem veriyi doğrular, satış metriklerini hesaplar, veri kalite problemlerini ve riskli müşterileri çıkarır, risk skoruna göre önceliklendirir, AI-like yönetici yorumu üretir ve raporları PDF/Markdown/CSV/JSON olarak indirilebilir hale getirir.

Uzun vadeli ürün ailesi:

1. **AI Virtual Data Analyst** — Excel'den yönetici raporu çıkarır.
2. **AI Virtual Data Engineer** — dağınık Excel/CSV verisini temizler, kolon eşler, standartlaştırır.
3. **AI Virtual Data Scientist** — satış tahmini, müşteri riski, anomali, segmentasyon ve fırsat analizi üretir.

Büyüme yönü:

- Önce satış/yönetici raporu.
- Sonra muhasebe/tahsilat raporu.
- Sonra stok/operasyon raporu.
- Sonra şirket bazında özelleştirilmiş çoklu rapor paketleri.
- En son SaaS platformu, kullanıcı hesabı, geçmiş raporlar, ödeme, şirketleşme ve ölçekleme.

---

## 1. Kullanıcının hedefi

Kullanıcının hedefi kariyer projesi yapmak değil, şirket kurmaktır. Bu nedenle Claude Code sadece kodu çalıştırmaya değil, ürünün satılabilir, demo yapılabilir ve müşteriyle test edilebilir hale gelmesine hizmet etmelidir.

Ana hedef:

> Çalışan MVP'yi, gerçek KOBİ kullanıcılarına gösterilebilecek ve ücretli pilot alınabilecek bir AI/data otomasyon ürününe dönüştürmek.

Kullanıcı şirketi hızlı büyütmek istiyor ancak ilk 18 aya kadar maaşlı eleman, freelance veya part-time destek almayabilir. Bu yüzden sistem tek kurucunun yönetebileceği kadar sade, otomasyonlu ve tekrar kullanılabilir olmalıdır.

---

## 2. Şirket vizyonu ve paketleme

### 2.1 Ana marka

**AI Virtual Data Team**

Kısa açıklama:

> Data ekibi olmayan şirketler için AI destekli sanal veri ekibi. Excel, CSV ve operasyon dosyalarını analiz eder; veri hatalarını bulur, yönetici raporları üretir, riskleri gösterir ve karar önerileri sunar.

### 2.2 Ürün paketleri

#### Paket 1 — AI Virtual Data Analyst

Müşteri dili:

> Excel dosyanı yükle, 5 dakikada yönetici raporu al.

İçerik:

- Excel yükleme
- Kolon doğrulama
- KPI kartları
- Toplam satış
- Kazanılan satış
- Bekleyen/kaybedilen satış sayıları
- Bölge/ürün/satış temsilcisi kırılımları
- Veri kalite problemleri
- Riskli müşteri listesi
- Risk Skoru ve Öncelik
- AI-like yönetici yorumu
- PDF/Markdown/CSV/JSON çıktı

Bu, mevcut çalışan MVP'nin ana paketidir ve ilk satılacak üründür.

#### Paket 2 — AI Virtual Data Engineer

Müşteri dili:

> Dağınık Excel ve CSV dosyalarını rapora hazır hale getirir.

İçerik:

- Farklı Excel kolon isimlerini tanıma
- Kolon eşleştirme
- Tutar/tarih/metin temizleme
- Veri tipi standardizasyonu
- Eksik kolon uyarısı
- Tekrarlı kayıt kontrolü
- Standart analiz formatına dönüştürme
- Temizlenmiş veri çıktısı

Bu paket v11/v12 ve sonraki adımlarla büyüyecektir.

#### Paket 3 — AI Virtual Data Scientist

Müşteri dili:

> Verinden tahmin, risk ve fırsat analizi çıkarır.

İçerik:

- Satış tahmini
- Tahsilat riski tahmini
- Müşteri kaybı/churn riski
- Ürün performans trendi
- Anomali tespiti
- Segmentasyon
- Fırsat önerileri

Bu paket hemen yapılmamalı; önce Analyst ve Engineer paketleri oturmalıdır.

---

## 3. Çoklu rapor vizyonu

Mevcut ürün satış/yönetici raporu üretmektedir. Uzun vadede sistem çoklu rapor motoruna dönüşmelidir.

Hedef rapor türleri:

1. **Satış / Yönetici Raporu**
   - Ciro, kazanılan satış, bekleyen satış, kaybedilen satış
   - Bölge/ürün/satış temsilcisi kırılımları
   - Riskli müşteriler
   - Veri kalite uyarıları

2. **Muhasebe / Finans Raporu**
   - Gelir/gider özeti
   - Açık bakiye
   - Geciken ödeme
   - Fatura/tahsilat durumu
   - Nakit akışı göstergeleri

3. **Tahsilat Raporu**
   - Geciken müşteriler
   - Öncelikli tahsilat listesi
   - Risk skoru
   - Tahsilat aksiyon önerileri

4. **Stok Raporu**
   - Azalan stoklar
   - Hızlı/yavaş dönen ürünler
   - Kritik stok seviyesi
   - Stok değer analizi

5. **Operasyon Raporu**
   - Süreç gecikmeleri
   - İş yükü
   - Hata oranları
   - Operasyonel riskler

6. **Şirkete Özel Rapor**
   - Şirketin kendi kolonlarına ve KPI'larına göre özel rapor
   - Config/ayar tabanlı olmalı, her müşteri için ayrı kod yazılmamalı

Önemli mimari prensip:

> Her rapor türü için tamamen ayrı uygulama yazma. Ortak upload/validation/mapping/analysis/reporting çekirdeği kur; rapor türlerini modül veya config olarak ekle.

Gelecek mimari örneği:

```text
report_types/
├── sales/
│   ├── schema.py
│   ├── analyzer.py
│   ├── summary.py
│   └── templates/
├── accounting/
├── collections/
├── stock/
├── operations/
└── custom/
```

---

## 4. Mevcut teknik durum

### 4.1 Genel durum

Mevcut proje Python + Streamlit tabanlı local web MVP'dir.

Ana akış:

```text
Kullanıcı Excel yükler
→ file_validator.py kolonları doğrular
→ app.py dosyayı data/Sales Demo Data.xlsx olarak kaydeder
→ analyze_sales.py analiz motoru çalışır
→ output klasöründe JSON, Markdown, PDF, CSV çıktıları oluşur
→ generate_ai_summary.py AI-like yönetici yorumu üretir
→ Streamlit ekranında KPI, AI yorum, teknik rapor, veri kalite ve risk tabloları gösterilir
→ kullanıcı raporları indirir
```

### 4.2 Mevcut önemli dosyalar

```text
app.py
```
Streamlit web arayüzü. Excel yükleme, analiz butonu, KPI kartları, sekmeler, rapor gösterimi ve indirme butonları burada yer alır.

```text
app_utils.py
```
Dosya okuma, JSON okuma, CSV güvenli okuma, AI summary başlığını temizleme, fonksiyon loglarını yakalama ve download button yardımcıları.

```text
file_validator.py
```
Excel şablonu oluşturma, kolon normalizasyonu, eksik kolon kontrolü, yüklenen Excel doğrulama ve mevcut Excel dosyasını analiz öncesi doğrulama.

```text
analyze_sales.py
```
Satış analiz motoru. Excel okur, satış tutarını temizler, KPI hesaplar, veri kalite sorunlarını bulur, riskli müşterileri çıkarır, risk skoru ve öncelik hesaplar, Markdown/PDF/CSV/JSON çıktıları üretir.

```text
generate_ai_summary.py
```
`analysis_result_v4.json` dosyasını okuyup local AI-like yönetici yorumu üretir. Dikkat: mevcut bazı sürümlerde `Atlas Holding` gibi hardcoded cümle kalmış olabilir. Bu dosya mutlaka kontrol edilmelidir.

```text
generate_ai_summary_api.py
```
OpenAI API entegrasyonu denemesi. Şimdilik aktif kullanılmamalıdır. API billing/quota nedeniyle beklemede. Gerçek API entegrasyonu müşteri doğrulaması veya ödeme sinyali gelmeden açılmamalı.

```text
generate_test_data.py
```
Clean, dirty ve large test Excel dosyalarını üretir.

```text
README.md
```
Proje açıklaması ve versiyon geçmişi. Yeni versiyonlar tamamlandıkça güncellenmelidir.

```text
.env
```
Gizli API key içerir. Asla paylaşma, commit etme, loglama veya dokümana yazma. Bu dosyada görünen key daha önce açığa çıkmış olabilir; güvenlik açısından rotate edilmelidir.

```text
.gitignore
```
`.env`, `__pycache__/`, `*.pyc` gibi dosyaları hariç tutmalıdır.

### 4.3 Beklenen klasör yapısı

Projede yerel geliştirmede aşağıdaki yapı hedeflenir:

```text
ai-virtual-data-analyst-demo/
├── app.py
├── app_utils.py
├── file_validator.py
├── analyze_sales.py
├── generate_ai_summary.py
├── generate_ai_summary_api.py
├── generate_test_data.py
├── README.md
├── .env
├── .gitignore
├── data/
│   └── Sales Demo Data.xlsx
├── output/
│   ├── analysis_result_v4.json
│   ├── ai_prompt_v5.txt
│   ├── generated_ai_summary_v5.md
│   ├── generated_report_v4.md
│   ├── generated_report_v4.pdf
│   ├── generated_report_v5.md
│   ├── data_quality_issues.csv
│   └── risky_customers.csv
└── test_data/
    ├── clean_sales_data.xlsx
    ├── dirty_sales_data.xlsx
    └── large_sales_data.xlsx
```

Not: ChatGPT ortamında dosyalar bazen tek klasörde düz şekilde durabilir. Claude Code gerçek repo kökünü inceleyerek mevcut yapıyı doğrulamalıdır.

---

## 5. Versiyon geçmişi ve mevcut ürün seviyesi

### v1 — İlk analiz motoru

Excel okundu; toplam satış, kazanılan satış, bölge/ürün/temsilci kırılımları çıkarıldı.

### v2 — Markdown + CSV çıktıları

Yönetici raporu, veri kalite sorunları CSV ve riskli müşteriler CSV oluşturuldu.

### v3 — PDF ve risk birleştirme

PDF rapor üretildi; aynı müşterinin birden fazla riski tek satırda birleştirildi.

### v4 — Structured JSON

`analysis_result_v4.json` üretildi; `nan` değerleri kullanıcı dostu şekilde temizlendi.

### v5 — AI-like yönetici yorumu

Local AI-like summary üretildi; teknik rapor yönetici diline çevrildi.

### v5.1 — OpenAI API denemesi

API entegrasyon kodu yazıldı; billing/quota olmadığı için beklemeye alındı.

### v6 — Streamlit web MVP

Excel yükleme, analiz etme, rapor gösterme ve indirme web ekranı kuruldu.

### v7 — Excel doğrulama

Şablon indirme, kolon kontrolü, dosya önizleme ve boş CSV güvenliği eklendi.

### v8.1 — Kullanıcı dostu indirme deneyimi

Teknik dosya isimleri yerine kullanıcı dostu dosya adları eklendi.

### v9.1-v9.6 — Kod mimarisi toparlama

`analyze_sales.py`, `generate_ai_summary.py`, `file_validator.py`, `app_utils.py` gibi dosyalar fonksiyonlaştırıldı ve sorumluluklar ayrıldı.

### v10.1 — Test dataları

Clean, dirty ve large test Excel dosyaları üretildi.

### v10.2 — Büyük veri testi

500 satırlık large data test edildi.

### v10.3 — Risk Skoru / Öncelik

Risk Skoru ve Öncelik kolonları eklendi. Riskli müşteriler skorla sıralanmaya başladı.

Son bilinen benchmark:

- Toplam satış: `67.700.256 TL`
- Kazanılan satış: `22.744.126 TL`
- Veri kalite problemi: `8`
- Riskli müşteri kaydı: `21`
- En güçlü bölge: `Antalya`
- En güçlü ürün: `Paket C`
- En güçlü temsilci: `Burak`
- En yüksek risk: `Nova Teknoloji`, Risk Skoru `11`, Öncelik `Yüksek`

### v10.4 — Planlanan UI iyileştirmesi

Risk tablosundaki uzun aksiyon metinleri kısaltılacak veya daha okunabilir hale getirilecek.

### v11 / v11.1 — Kolon eşleştirme ekranı

Konuşma durumuna göre kullanıcı v11.1'in çalıştığını söylemiştir. Ancak Claude Code mevcut repo dosyalarını inceleyip bu özelliğin gerçekten kodda olup olmadığını doğrulamalıdır. Eğer mevcut kodda yoksa v11/v11.1 ayrı küçük adımlarla uygulanmalıdır.

---

## 6. Önemli bilinen açıklar ve dikkat noktaları

### 6.1 `generate_ai_summary.py` hardcoded müşteri sorunu

Bazı sürümlerde AI Yönetici Yorumu içinde şu tarz eski hardcoded cümle bulunabilir:

```text
Atlas Holding gibi anormal yüksek görünen kayıtlar...
```

Bu yanlış davranıştır. AI summary, JSON içindeki gerçek riskli müşterilere göre dinamik olmalıdır.

Doğru davranış:

- `risks.customers` listesini Risk Skoru'na göre sırala.
- `Risk Tipi` içinde `Anormal yüksek satış` geçen müşteri varsa gerçek müşteri adını yaz.
- Yoksa anormal yüksek satış varmış gibi davranma.
- JSON'da olmayan müşteri uydurma.

Öncelikli teknik görevlerden biri budur.

### 6.2 API key güvenliği

`.env` dosyası gizli bilgi içerir. Claude Code hiçbir koşulda API key'i yazdırmamalı, dokümana kopyalamamalı, commit etmemeli veya loglamamalıdır.

Güvenli davranış:

- `.env` `.gitignore` içinde olmalı.
- Gerçek API entegrasyonu kapalı kalmalı.
- Key açığa çıktıysa kullanıcıya rotate önerilmeli.
- Demo/test local AI-like summary ile devam etmeli.

### 6.3 Scope creep riski

Kullanıcı büyük vizyon istiyor: Analyst + Engineer + Scientist + çoklu raporlar. Ancak geliştirme küçük versiyonlarla ilerlemelidir.

Altın kural:

> Her seferinde çalışan ürünü bozmadan, tek küçük versiyon ekle.

Yanlış:

- Bir anda FastAPI + React + SaaS + login + billing + tüm rapor türleri yapmak.

Doğru:

- Mevcut Streamlit MVP'yi koru.
- Önce mevcut Analyst paketini demo kalitesine çıkar.
- Sonra kolon eşleştirme/farklı Excel formatları.
- Sonra ikinci rapor türü.
- Sonra müşteri/pilot doğrulamasına göre büyüt.

---

## 7. Claude Code çalışma prensipleri

Claude Code bu projede aşağıdaki kurallara uymalıdır:

1. **Önce oku, sonra değiştir.**
   - `README.md`
   - `app.py`
   - `file_validator.py`
   - `analyze_sales.py`
   - `generate_ai_summary.py`
   - `app_utils.py`

2. **Büyük rewrite yapma.**
   - Kullanıcı öğrenerek ilerliyor.
   - Mevcut çalışan kodu koru.
   - Küçük, versiyon bazlı değişiklik yap.

3. **Her değişiklikten sonra test et.**
   - Import hatası var mı?
   - Streamlit çalışıyor mu?
   - Excel upload çalışıyor mu?
   - Output dosyaları oluşuyor mu?

4. **Versiyon mantığını koru.**
   - v10.3, v10.4, v11, v11.1, v12 gibi net adımlarla ilerle.
   - README'ye kısa not ekle.

5. **Müşteri/demoya göre düşün.**
   - Kod sadece teknik olarak doğru değil, müşteri gözüyle anlaşılır olmalı.
   - Hata mesajları sade olmalı.
   - PDF ve rapor kullanıcıya sunulabilir olmalı.

6. **Gizlilik ve KVKK hassasiyeti.**
   - Gerçek müşteri verisi kullanılmamalı.
   - Demo/sentetik veri kullanılmalı.
   - İleride müşteri verisi alınırsa anonimleştirme ve sözleşme gerekebilir.

7. **OpenAI API'yi kendiliğinden aktif etme.**
   - Billing/quota hazır değil.
   - Ücretli API müşteri doğrulaması ve açık kullanıcı onayı olmadan açılmamalı.

8. **Çıktı dosyalarını dikkatli yönet.**
   - Demo çıktıları faydalı olabilir.
   - Gerçek müşteri çıktıları commit edilmemelidir.

---

## 8. Kurulum ve çalıştırma rehberi

### 8.1 Gerekli paketler

Temel paketler:

```bash
pip install pandas openpyxl streamlit fpdf python-dotenv openai
```

Not: API kullanılmayacaksa `openai` zorunlu olmayabilir. PDF için `fpdf` kullanılıyor.

### 8.2 Test datalarını üretme

```bash
python generate_test_data.py
```

Bu komut `test_data/` altında şunları üretir:

```text
clean_sales_data.xlsx
dirty_sales_data.xlsx
large_sales_data.xlsx
```

### 8.3 Streamlit uygulamasını başlatma

```bash
streamlit run app.py
```

### 8.4 Analiz motorunu doğrudan çalıştırma

```bash
python analyze_sales.py
```

Beklenen çıktılar:

```text
output/generated_report_v4.md
output/generated_report_v4.pdf
output/analysis_result_v4.json
output/data_quality_issues.csv
output/risky_customers.csv
```

### 8.5 AI-like summary üretme

```bash
python generate_ai_summary.py
```

Beklenen çıktılar:

```text
output/ai_prompt_v5.txt
output/generated_ai_summary_v5.md
output/generated_report_v5.md
```

### 8.6 Hızlı syntax kontrolü

```bash
python -m compileall .
```

---

## 9. Test senaryoları

Claude Code her anlamlı değişiklikten sonra en azından aşağıdaki testleri düşünmelidir.

### Test 1 — Clean data

Amaç:

- Temiz dosyada sistem hata vermeden rapor üretmeli.
- Risk/veri kalite sonucu dosyaya göre düşük veya boş olabilir.
- UI boş CSV durumunda bozulmamalı.

### Test 2 — Dirty data

Amaç:

- Eksik tutar yakalanmalı.
- Eksik bölge yakalanmalı.
- Eksik satış temsilcisi yakalanmalı.
- Hatalı tarih yakalanmalı.
- Negatif satış tutarı yakalanmalı.
- Standart dışı durum değeri yakalanmalı.
- Durum/ödeme tutarsızlığı yakalanmalı.
- Anormal yüksek satış yakalanmalı.

### Test 3 — Large data

Amaç:

- 500 satırlık veriyle performans makul olmalı.
- KPI kartları dolmalı.
- Risk skoru ve öncelik görünmeli.
- PDF/CSV/JSON/Markdown oluşmalı.
- AI summary gerçek riskli müşterileri kullanmalı.

Son bilinen large data benchmark:

```text
Toplam satış: 67.700.256 TL
Kazanılan satış: 22.744.126 TL
Veri kalite problemi: 8
Riskli müşteri: 21
Top region: Antalya
Top product: Paket C
Top sales rep: Burak
Top risk customer: Nova Teknoloji, skor 11
```

Eğer test data yeniden random üretilirse sayılar değişebilir. Bu nedenle benchmark mevcut dosyalar için referanstır, mutlak test assertion değildir.

### Test 4 — AI summary hardcoded kontrolü

Aşağıdaki arama yapılmalı:

```bash
grep -R "Atlas Holding" -n .
```

Eğer `generate_ai_summary.py` içinde hardcoded müşteri adı geçiyorsa düzeltilmelidir. Test çıktılarında geçmiş veriden dolayı Atlas Holding geçebilir; önemli olan kodun hardcoded olmamasıdır.

### Test 5 — Güvenlik kontrolü

```bash
git status
cat .gitignore
```

Kontrol:

- `.env` commitlenmiyor mu?
- `__pycache__/` hariç mi?
- Gerçek müşteri verisi yok mu?

---

## 10. Öncelikli teknik roadmap

### Bugünkü / çok yakın görevler

1. `.env` ve güvenlik kontrolü.
2. `generate_ai_summary.py` içinde hardcoded müşteri adı kalmadığını kontrol et ve düzelt.
3. Streamlit uygulamasını çalıştır.
4. Clean / dirty / large test dosyalarıyla test et.
5. Risk Skoru ve Öncelik kolonlarının UI'da göründüğünü doğrula.
6. AI Yönetici Yorumu'nun gerçek risk skorlarını kullandığını doğrula.
7. README'yi mevcut duruma göre güncelle.
8. Demo çıktıları klasörü hazırla.

### v10.4 — Risk tablosu okunabilirliği

- `Önerilen Aksiyon` çok uzunsa tabloyu bozabilir.
- Çözüm seçenekleri:
  - Kısa aksiyon özeti kolonu eklemek.
  - Uzun aksiyonu expander/detail olarak göstermek.
  - Risk tablosunda `Risk Özeti`, `Risk Skoru`, `Öncelik` odaklı görünüm yapmak.

### v11 / v11.1 — Kolon eşleştirme

Amaç:

- Kullanıcı farklı kolon adlarıyla Excel yükleyebilsin.
- Sistem alanları ile dosya kolonları eşleşsin.

Örnek mapping:

```text
Cari Adı → Müşteri
Net Ciro → Satış Tutarı
Fatura Tarihi → Tarih
Satışçı → Satış Temsilcisi
Şehir → Bölge
```

Beklenen yapı:

- Zorunlu sistem kolonları listelenir.
- Kullanıcı her sistem kolonu için Excel kolonu seçer.
- Eşleştirme sonrası dataframe sistem kolonlarına rename edilir.
- Analiz motoru yine standart kolonlarla çalışır.

### v12 — Farklı Excel formatları

- Satış, muhasebe/tahsilat gibi farklı formatlara hazırlık.
- Kolon eşleştirme kayıtları gelecekte müşteri bazında saklanabilir.

### v13 — Profesyonel PDF rapor tasarımı

- Kurumsal kapak
- KPI kartları
- Yönetici özeti
- Risk tablosu
- Veri kalite özeti
- Logo alanı
- Daha okunabilir tablo düzeni

### v14 — Demo deploy

- Streamlit Cloud / Render benzeri basit deploy.
- Gerçek müşteri verisi kullanılmamalı.
- Demo verisi sentetik olmalı.

### v15 — Gerçek AI API entegrasyonu

- Ancak müşteri doğrulaması, billing ve kullanıcı onayı sonrası.
- Local AI-like summary şimdilik yeterlidir.

### v16+ — SaaS altyapısı

- Kullanıcı hesabı
- Dosya geçmişi
- Rapor geçmişi
- Çoklu şirket
- Storage
- Auth
- Billing
- Güvenlik/KVKK

Bu aşamaya ilk müşteri sinyali gelmeden geçilmemelidir.

---

## 11. Önerilen gelecekteki teknik mimari

Kısa vadede mevcut Streamlit korunur. Orta vadede kod şu şekilde ayrılabilir:

```text
core/
├── file_io.py
├── validation.py
├── mapping.py
├── cleaning.py
├── scoring.py
├── report_writer.py
└── pdf_writer.py

report_types/
├── sales/
│   ├── schema.py
│   ├── analyzer.py
│   ├── recommendations.py
│   └── ai_summary.py
├── accounting/
├── collections/
├── stock/
└── operations/

app.py
settings.py
```

Ama bu refactor hemen yapılmamalı. Önce mevcut ürün çalışır şekilde kalmalı; refactor ihtiyaç doğdukça küçük adımlarla yapılmalı.

---

## 12. İş modeli ve pazarlama bağlamı

Claude Code ağırlıklı teknik çalışsa da ürün kararlarında iş bağlamını bilmelidir.

### 12.1 İlk hedef müşteri

- BI/data ekibi olmayan KOBİ'ler
- Şirket sahibi / genel müdür
- Satış yöneticisi
- Finans/muhasebe sorumlusu
- Operasyon yöneticisi
- Excel ile aylık rapor hazırlayan ekipler

### 12.2 İlk satış cümlesi

> Excel raporlarınızı 5 dakikada yönetici raporuna çeviren AI destekli sanal veri ekibi.

### 12.3 İlk gelir modeli

İlk gelir SaaS aboneliğinden değil, büyük ihtimalle ürünleşmiş hizmetten gelir:

- Tek rapor/pilot çalışma
- Müşteriye özel rapor kurulumu
- Aylık rapor otomasyonu
- İleride abonelik

### 12.4 Başarı metrikleri

- Upload başarı oranı
- Analiz tamamlanma süresi
- Rapor indirme oranı
- Kullanıcının "bu rapor işime yarar" deme oranı
- Tekrar kullanım
- Ödeme isteği
- Pilot müşteri sayısı

---

## 13. Şirketleşme bağlamı

Kullanıcı şirket kurmak istiyor ancak hemen şirket açmak istemiyor. Şirketleşme eşiği:

> Müşteri ücretli pilot istediğinde, fatura gerektiğinde veya gerçek şirket verisi sözleşmeyle alınacağında mali müşavirle şirketleşme adımı başlar.

Zamanlama hedefi:

- Haziran-Temmuz 2026: Founder gibi çalışma, demo ve ürün hazırlığı.
- Temmuz-Ağustos 2026: `Founder / Building AI Virtual Data Team` unvanı makul hale gelir.
- Eylül-Aralık 2026: İlk pilot/fatura sinyali olursa şirketleşme masaya gelir.
- 2027: Düzenli gelir oluşursa şirket yapısı ve operasyon oturur.

Claude Code'un bu konuda yasal/vergi tavsiyesi vermemesi gerekir; mali müşavir/hukuk uzmanına yönlendirilmelidir.

---

## 14. Kullanıcıyla çalışma tarzı

Kullanıcı hızlı ilerlemek istiyor. Claude Code şu tarzda çalışmalı:

- Küçük adımlar.
- Net dosya değişiklikleri.
- Her adımda hangi dosya değiştiğini söyle.
- Kod vermeden önce mevcut yapıyı analiz et.
- Hata olursa panik yapmadan izole et.
- Çalışan kodu bozma.
- Kullanıcı öğrenmek istiyor; kısa açıklama ekle.
- Uzun teorik mimariye gömülme; pratik ve versiyon bazlı ilerle.

Örnek iyi cevap:

```text
v10.4 için sadece risk tablosundaki aksiyon görünümünü düzelteceğim.
Değişecek dosya: app.py
Analiz motoruna dokunmayacağım.
Test: large_sales_data ile Riskli Müşteriler tabını kontrol edeceğiz.
```

Örnek kötü cevap:

```text
Tüm projeyi FastAPI + React + PostgreSQL'e çevirelim.
```

---

## 15. Bugün başlanacaksa önerilen sırayla görevler

1. Proje kökünde dosyaları listele.
2. `.env` ve `.gitignore` güvenliğini kontrol et; API key yazdırma.
3. `grep -R "Atlas Holding" -n .` ile hardcoded metin kontrolü yap.
4. `generate_ai_summary.py` dosyasını dinamik risk/outlier yorumuna çevir.
5. `python -m compileall .` çalıştır.
6. Gerekli klasörler yoksa `data/`, `output/`, `test_data/` yapısını doğrula.
7. Test dosyalarıyla analiz çalıştır.
8. Streamlit uygulamasını aç.
9. AI summary, Risk Skoru ve Öncelik görünümünü kontrol et.
10. README'ye yapılan versiyon notunu ekle.

---

## 16. Definition of Done

Bir versiyon ancak şu koşullarda tamamlanmış sayılır:

- Uygulama açılıyor.
- Excel yükleme çalışıyor.
- Analiz Et butonu hata vermiyor.
- KPI kartları doluyor.
- AI Yönetici Yorumu oluşuyor.
- Teknik rapor oluşuyor.
- Veri Kalitesi tabı boş/filled durumda bozulmuyor.
- Riskli Müşteriler tabında Risk Skoru ve Öncelik görünüyor.
- PDF/Markdown/CSV/JSON indirme dosyaları oluşuyor.
- README güncel.
- Hardcoded müşteri adı yok.
- `.env` güvenli.

---

## 17. Kısa Claude Code promptu

Claude Code'a hızlı başlatma için aşağıdaki prompt verilebilir:

```text
Bu projede AI Virtual Data Team üzerinde çalışıyorsun. Önce proje kökündeki CLAUDE.md dosyasını oku. Mevcut MVP Streamlit + Python tabanlı AI Virtual Data Analyst ürünüdür. Amacımız çalışan kodu bozmadan, küçük versiyonlarla ürünü demo/pilot müşteri seviyesine getirmek. Önce dosyaları incele, sonra sadece istenen göreve dokun. .env içeriğini asla yazdırma. OpenAI API'yi kendiliğinden aktif etme. Her değişiklik sonrası compile/test öner. İlk teknik öncelik: generate_ai_summary.py içinde hardcoded müşteri adı kalmaması ve risk skoru/öncelik mantığına göre dinamik AI-like summary üretilmesi.
```

---

## 18. En önemli stratejik kural

> Bu proje kod projesi değil, şirketleşme adayıdır. Kod kararları müşteri demosu, pilot görüşme ve ücretli kullanım ihtimalini artıracak şekilde alınmalıdır.

