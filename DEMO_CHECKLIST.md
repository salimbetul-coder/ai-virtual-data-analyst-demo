# Demo Checklist — Müşteri/Yatırımcı Sunumu

AI Virtual Data Analyst'i potansiyel müşteri, pilot kullanıcı veya yatırımcıya gösterirken bu checklist'i takip et. Hedef süre: **5-7 dakikalık akıcı demo**.

**Canlı demo URL:** https://ai-virtual-data-analyst.streamlit.app

---

## 1. Demo öncesi (toplantıdan 1 saat önce)

### Teknik hazırlık

- [ ] Cloud demo URL'i aç → 3-5 saniye içinde yükleniyor mu? (cold start ısıtmak için)
- [ ] Demo URL'inde **"Hazır demo raporu bulundu"** mesajı görünüyor mu (önceki analiz cache'li)
- [ ] Toplam Satış kartı `67.700.256 TL` gösteriyor mu — bu sayı CLAUDE.md'deki referans değerdir
- [ ] AI Yönetici Yorumu sekmesi açılıyor; bölüm 2'de Nova Teknoloji görünüyor
- [ ] PDF Yönetici Raporu indirilebiliyor → indirip Türkçe karakterleri (ş, ı, ğ, ç) gözle kontrol et

### Yedek planı

- [ ] Lokal makinende `streamlit run app.py` çalıştırabilir durumda olmalı (cloud düşerse)
- [ ] `demo_outputs/` klasöründeki donmuş showcase dosyalarını bilgisayarda hızlı erişilebilir bir yerde tut:
  - `demo_pdf_yonetici_raporu.pdf` — internet kesilirse direkt göster
  - `demo_ai_yonetici_yorumu.md` — AI yorumun nasıl olduğu örnek
  - `demo_riskli_musteriler.csv` — risk listesi formatı
- [ ] Yedek senaryo Excel'leri:
  - `test_data/large_sales_data.xlsx` — etkileyici demo veri
  - Hazırladığın "müşteri tarzı" custom Excel (farklı kolon adlarıyla — kolon eşleştirme demosu için)

### Mesaj hazırlığı

- [ ] 30 saniyelik **elevator pitch**'in netleşmiş olmalı:
  > "BI/data ekibi olmayan KOBİ'ler Excel raporlarını saatlerce manuel hazırlıyor. AI Virtual Data Analyst, yüklenen Excel'i 5 dakikada yönetici raporuna çevirir; veri hatalarını, riskli müşterileri ve aksiyon önerilerini otomatik çıkarır. Bu da bir 'sanal veri analisti' gibi çalışır."

- [ ] Müşterinin profiline göre **odak noktasını** seç:
  - Yönetici/CEO → AI Yorum + KPI kartları
  - Finans/muhasebe → Veri Kalite + Riskli Müşteriler
  - Operasyon → Tablo kırılımları + aksiyon planı
  - Teknik karar verici → Mimari basitlik, deploy edebilirlik

---

## 2. Demo akışı (5-7 dk)

### Adım 1 — Açılış (30 sn)

> "Şu URL üzerinden canlı çalışıyor: ai-virtual-data-analyst.streamlit.app"

- Demoyu projeksiyon/ekran paylaşımında aç
- Sayfayı yenilemeyle başlama; "Hazır demo raporu bulundu" mesajını göster
- **Söyle:** "Bir KOBİ Excel'ini yükledikten sonra şu çıktıları otomatik alır — şimdi mevcut demo veri üzerinden gösteriyorum."

### Adım 2 — KPI kartları (45 sn)

- Sayfayı yukarı kaydır, **Genel Durum** bölümünü göster
- 4 KPI kartı: Toplam Satış, Kazanılan, Veri Kalite Problemi, Riskli Müşteri
- **Söyle:** "67 milyon TL'lik bir satış hacminden geçen ay 22 milyonu kazanıldı. Ama veride 8 kalite problemi ve 21 takip edilmesi gereken müşteri var. Sistem bunları tek tıkla çıkarıyor."

### Adım 3 — AI Yönetici Yorumu (90 sn) ⭐ ANA NOKTA

- "AI Yönetici Yorumu" sekmesine geç
- Bölüm 2 "Dikkat Edilmesi Gereken Ana Riskler"'i göster
- **Söyle:** "Bu yorum hazır değil, AI tarafından her dosyaya göre yeniden üretiliyor. Mesela burada Nova Teknoloji 11 risk skoruyla işaretlendi — çünkü geciken ödeme + durum tutarsızlığı + anormal yüksek satış üçlüsü var. Sistem otomatik bunu yönetici diline çevirip aksiyon önerdi."
- Bölüm 4 "Öncelikli Aksiyon Planı"'na in
- **Söyle:** "Bu 5 aksiyon, raporu okuyan yöneticinin pazartesi sabahı yapması gereken konkrete işleri söylüyor."

### Adım 4 — Riskli Müşteriler tablosu (60 sn)

- "Riskli Müşteriler" sekmesine geç
- Öncelik filtresinde "Yüksek"i seç
- **Söyle:** "Yüksek öncelikli 4 müşteri var — Nova Teknoloji, Mira Perakende, Eksen Otomotiv, Star Medya. Tahsilat ekibi sabah bu listeyle başlasa o gün kaç müşteriye dönmesi gerektiğini biliyor."
- "Detaylı aksiyon metinlerini göster" expander'ını aç → uzun aksiyon metinlerini göster
- **Söyle:** "Müşteri bazında ne yapılması gerektiği de yazılı."

### Adım 5 — PDF Yönetici Raporu (60 sn) ⭐ "VAY!" ANI

- "İndir" sekmesine geç
- **"PDF Yönetici Raporu"** butonuna tıkla → indirilen PDF'i aç
- 6 sayfayı hızlıca geç:
  - Kapak (mavi şerit + büyük başlık)
  - KPI kartları + yönetici özeti
  - Risk tablosu (renkli pill badge'ler)
  - Veri kalite tablosu
  - Performans kırılımları
  - Aksiyon planı
- **Söyle:** "Bu PDF herhangi bir yönetim toplantısına direkt sunulabilir. Müşteri yöneticisi, finans direktörü, hatta CEO seviyesine."

### Adım 6 — Kolon Eşleştirme (60 sn) — KOBİ farklılaşması

- **Söyle:** "Şimdi gerçek bir KOBİ senaryosuna bakalım. Çünkü her firmanın Excel'i farklı kolon adlarıyla geliyor — `Cari Adı`, `Net Ciro`, `Fatura Tarihi` gibi."
- Önceden hazırladığın custom Excel'i upload et
- Kolon eşleştirme ekranı çıkar
- **Söyle:** "Sistem otomatik öneri yapıyor — bir kez eşleştirip kaydedersen aynı dosya yapısı için bir daha eşleştirmeye gerek kalmıyor."
- "Kolonları Eşleştir ve Kaydet" → yeşil onay
- **Söyle:** "Bu sistem firmanın özel Excel formatını öğreniyor."

### Adım 7 — Kapanış (30 sn)

- **Söyle:**
  > "Özetle: bu sistem bir veri analistinin haftalarca yapacağı işi 5 dakikaya indiriyor. Sıfırdan kurulum gerektirmiyor, müşteri sadece Excel yüklüyor. Pilot olarak sizin verilerinizle test edebiliriz."
- Sonraki adım sor: "Sizde bir pilot Excel ile deneyebilir miyiz?"

---

## 3. Müşterinin sorabileceği yaygın sorular

### "Verim güvende mi?"

- Demo dosyaları **sentetik**, gerçek müşteri verisi yok
- Cloud demo Streamlit Cloud üzerinde, ama pilot için **on-premise** veya **self-hosted** kurulum mümkün
- Geçici kullanım — analiz sonrası veri saklanmıyor (mapping memory hariç, o da kolon adlarıdır, müşteri içeriği değil)
- KVKK uyumu için sözleşme aşamasında ayrıca konuşulur

### "AI hangi modeli kullanıyor?"

- Şu an **lokal AI-like summary** (kural-tabanlı yönetici yorumu, internet/API gerektirmez)
- Müşteri pilotu sonrası OpenAI / Anthropic Claude API entegrasyonu açılabilir
- Bu da API maliyetinin müşteri tarafından mı yoksa SaaS tarafından mı karşılanacağına bağlı

### "Bizim Excel'imiz farklı, çalışır mı?"

- **Evet** — kolon eşleştirme ekranı standart olmayan kolonları tanıyor
- Mevcut destek: `Cari Adı`, `Net Ciro`, `Fatura Tarihi`, `Satışçı`, `Şehir` gibi yaygın varyantlar otomatik eşleşir
- Pilot sırasında özel kolon adlarınız da öğretilebilir

### "Sadece satış mı? Bizim muhasebe/stok/operasyon raporlarımız var."

- Şu an **satış/yönetici raporu** odaklı
- Mimari çoklu rapor desteğine hazır (`report_schemas/` modüler)
- v12 ile zemin kuruldu; ikinci rapor türü (muhasebe veya tahsilat) pilot talebiyle birlikte eklenir

### "Fiyatı ne?"

- Şu aşamada **pilot fiyatlaması** konuşulur, abonelik henüz yok
- Tek bir pilot rapor kurulumu, aylık otomasyon, veya özel rapor şablonu — ihtiyaca göre paket
- Detay sözleşme aşamasında belirlenir

### "Kim geliştiriyor? Ekip ne büyüklükte?"

- Şu an solo kurucu tarafından geliştiriliyor
- Pilot büyüklüğüne göre ekip genişletilir
- Vizyon: AI Virtual Data Team — Analyst, Engineer, Scientist ürün ailesi

---

## 4. Demo bitmeden mutlaka yapılacaklar

- [ ] Müşterinin **e-mail adresini** al
- [ ] Sonraki adım için **takvim daveti** öner (3 gün içinde)
- [ ] PDF Yönetici Raporu örneğini müşteriye **e-mail ile** gönder (demo PDF zaten hazır: `demo_outputs/demo_pdf_yonetici_raporu.pdf`)
- [ ] Müşterinin Excel formatından **örnek 1 dosya** istemesini sağla (NDA gerekiyorsa konuş)

---

## 5. Demo sonrası 24 saat içinde

- [ ] Teşekkür e-maili gönder (demo PDF eklenmiş olsun)
- [ ] Müşterinin sorduğu özel sorular için **kişisel cevap** ekle (genel cevap değil)
- [ ] Pilot öneri belgesi taslağı yaz (3 madde: kapsam, süre, fiyat)
- [ ] Sıradaki takip günü için kendine hatırlatma kur

---

## 6. Hata anında ne yapacaksın

### Cloud yavaş veya hata verdi

- **Söyle:** "Cloud kısa süreliğine cevap vermiyor. Aynı demoyu lokalde göstereyim."
- Lokal `streamlit run app.py` aç → aynı akışı tekrarla

### Internet yok / projeksiyon hatası

- **Söyle:** "Önceden hazırladığım PDF örneği üzerinden anlatayım."
- `demo_outputs/demo_pdf_yonetici_raporu.pdf` aç → 6 sayfayı sunum gibi göster
- AI yorum içeriği için `demo_outputs/demo_ai_yonetici_yorumu.md`'yi metin olarak oku

### Müşteri yanlış format Excel yükledi

- **Söyle:** "Sistem zaten farklı kolonları kolayca tanır" — kolon eşleştirme ekranını canlı kullan
- Bu aslında demonun **güçlü yanı** — hatadan avantaj çıkarmış olursun

### Beklenmeyen sayı / sonuç

- Panik etme; demo verisi sentetik, gerçek müşteri parası değil
- **Söyle:** "Bu sayılar şu anki test verisine ait, gerçek pilot'ta sizin verinizle gerçek sonuç gelecek."

---

## 7. Demo sonrası kendi geri bildirimini yaz

Her demo sonrası 5 dakika ayır ve şunları kaydet:

- Müşteri en çok **hangi noktaya** ilgi gösterdi?
- En çok **hangi sorunsoruldu**?
- Hangi özelliği **anlamadı/atladı**?
- Sonraki demoda **neyi değiştirmeli/eklemelisin**?

Bu notları zamanla biriktir — ürün yol haritası için en değerli geri bildirim kaynağıdır.
