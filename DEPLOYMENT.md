# Deployment Rehberi — Streamlit Cloud

Bu döküman v14 MVP'sini Streamlit Cloud üzerinde halka açık demo olarak deploy etmek içindir. Mevcut canlı demo: https://ai-virtual-data-analyst.streamlit.app

## İçerik

1. [Pre-deploy checklist](#1-pre-deploy-checklist)
2. [Streamlit Cloud üzerinde deploy](#2-streamlit-cloud-üzerinde-deploy)
3. [Post-deploy doğrulama](#3-post-deploy-doğrulama)
4. [Güncelleme / yeniden deploy](#4-güncelleme--yeniden-deploy)
5. [Yaygın hatalar ve çözümler](#5-yaygın-hatalar-ve-çözümler)
6. [Güvenlik notları](#6-güvenlik-notları)
7. [Alternatif platformlar](#7-alternatif-platformlar)

---

## 1. Pre-deploy checklist

Deploy etmeden önce şunların tümünün repo'da olduğunu doğrula:

### Zorunlu dosyalar

- [ ] `app.py` — Streamlit ana giriş noktası
- [ ] `requirements.txt` — 4 paket: `streamlit>=1.32`, `pandas>=2.0`, `openpyxl>=3.1`, `fpdf2>=2.7`
- [ ] `data/Sales Demo Data.xlsx` — bundled demo veri (sentetik)
- [ ] `fonts/DejaVuSans.ttf` + `fonts/DejaVuSans-Bold.ttf` — Türkçe karakter desteği için bundled TTF
- [ ] `.streamlit/config.toml` — kurumsal tema + upload limit + telemetri kapatma
- [ ] `report_schemas/sales.py` — kolon şeması
- [ ] Tüm Python kaynak dosyaları (`analyze_sales.py`, `generate_ai_summary.py`, `file_validator.py`, `app_utils.py`)

### Zorunlu olarak yok olması gerekenler

- [ ] `.env` — repo'da OLMAMALI; lokal kalmalı, gitignored olmalı
- [ ] Gerçek müşteri verisi — sadece sentetik `test_data/` ve `data/Sales Demo Data.xlsx`
- [ ] Hardcoded API key veya credentials — kaynak kodda olmamalı
- [ ] `output/` runtime artifact'ları — gitignored, deploy etmemeli

### Doğrulama komutları

```powershell
# 1. requirements.txt'in doğru olduğunu test et
python -m compileall .

# 2. Lokal Streamlit ile uçtan uca test
streamlit run app.py
# Tarayıcıda http://localhost:8501 → "Analiz Et" → 67.700.256 TL benchmark

# 3. .env sızıntı kontrolü
git ls-files .env                              # boş çıkmalı (tracked değil)
git log --all --full-history -- .env           # boş çıkmalı (history'de yok)
git check-ignore -v .env                       # .gitignore:2:.env

# 4. PDF Türkçe karakter kontrolü
python analyze_sales.py                        # output/generated_report_v4.pdf üretmeli
# PDF'i aç → ş/ı/ğ/ç doğru render edilmiş mi

# 5. Font dosyaları repo'da mı
git ls-files fonts/                            # 2 dosya listelemeli
```

Tüm checklist tamamsa devam et.

---

## 2. Streamlit Cloud üzerinde deploy

### Ön koşul: GitHub repo

Kod **public bir GitHub repo'da** olmalı. Streamlit Cloud free tier sadece public repo destekler.

Mevcut repo: `https://github.com/<kullanıcı-adın>/ai-virtual-data-analyst-demo`

### Adım 1 — Streamlit Cloud hesabı

1. https://share.streamlit.io adresine git
2. **"Continue with GitHub"** ile giriş yap
3. GitHub OAuth onay sayfasında **kodun bulunduğu hesabı** seçtiğinden emin ol
4. Streamlit Cloud workspace'in açıldığını gör

### Adım 2 — GitHub App izni (ilk defaysa)

Streamlit Cloud repo dosyalarına erişmek için bir GitHub App kullanır.

1. https://github.com/apps/streamlit adresine git
2. **"Install"** veya **"Configure"** butonuna bas
3. Doğru hesabı seç → **"All repositories"** veya sadece bu repo'yu seç
4. **"Install"** butonuna bas

### Adım 3 — Yeni uygulama oluştur

1. Streamlit Cloud workspace'de **"Create app"** veya **"New app"** butonuna bas
2. Form alanları:
   - **Repository:** `<kullanıcı-adın>/ai-virtual-data-analyst-demo`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **App URL (opsiyonel):** `ai-virtual-data-analyst` (kullanışlı bir slug, müşteriye paylaşılabilir)
3. **Advanced settings** kısmına dokunma — Python sürümü, secrets gerekmiyor (`.env` yok)
4. **"Deploy"** butonuna bas

### Adım 4 — Build izle

Build logu sağ tarafta akar. 2-3 dakika sürer. Sırayla şu adımları görürsün:

```
Cloning repository...
Setting up dependencies...
Installing requirements.txt...
  streamlit>=1.32
  pandas>=2.0
  openpyxl>=3.1
  fpdf2>=2.7
Starting up server...
Your app is now live!
```

Son satırı görünce URL'in: `https://<slug>.streamlit.app`

---

## 3. Post-deploy doğrulama

Build başarılı olduğunda 8-maddelik **acil smoke test**'i 2 dakikada yap:

1. [ ] URL açılıyor mu? (`https://ai-virtual-data-analyst.streamlit.app`)
2. [ ] Sayfa başlığı **"AI Virtual Data Analyst"** ve light tema mı?
3. [ ] **"Hazır demo raporu bulundu"** veya **"Henüz rapor oluşmadı"** info mesajı görünüyor mu?
4. [ ] **"Örnek Excel Şablonunu İndir"** butonu Excel indiriyor mu?
5. [ ] **"Analiz Et"** kırmızı butonuna bas — bundled demo veri ile analiz başarılı mı?
6. [ ] KPI kartları görünüyor mu? (Cloud cold start sonrası 67.700.256 TL beklenir)
7. [ ] **"İndir"** sekmesinden **PDF Yönetici Raporu**'nu indir — PDF açılıyor mu, Türkçe karakterler (ş, ı, ğ, ç) doğru mu?
8. [ ] **AI Yönetici Yorumu** sekmesi — "Nova Teknoloji (Yüksek, skor: 11)" yazıyor mu?

Detaylı testler için: [TESTING.md](TESTING.md).

---

## 4. Güncelleme / yeniden deploy

Streamlit Cloud `main` branch'i izler. Yeni değişiklik için:

```powershell
git add <değişen dosyalar>
git commit -m "<commit mesajı>"
git push origin main
```

Push'tan **30-60 saniye sonra** Streamlit Cloud otomatik yeniden deploy başlatır. Manuel müdahale gerekmez.

### Yeniden deploy logu izleme

1. https://share.streamlit.io → uygulamana git
2. Sağ alt **"Manage app"** → **Logs** sekmesi
3. "Updated repository..." → "Restarting..." → "Your app is now live!" satırlarını gör

### Manuel reboot gerekirse

Bir sebepten otomatik yeniden deploy başlamadıysa veya uygulama takıldıysa:

1. **"Manage app"** menüsüne git
2. Sağ üst **"⋮"** menü → **"Reboot app"**
3. 30 saniye bekle

---

## 5. Yaygın hatalar ve çözümler

### ❌ "ModuleNotFoundError: No module named X"

Build logunda `requirements.txt`'te eksik bir paket var.

**Çözüm:** Lokal'de `pip freeze | grep <paket>` ile sürümü öğren, `requirements.txt`'e ekle, push'la.

### ❌ "FileNotFoundError: data/Sales Demo Data.xlsx"

`data/` klasörü deploy'a dahil olmamış (gitignored olduğu için, ya da hiç eklenmediği için).

**Çözüm:**
```powershell
git check-ignore -v "data/Sales Demo Data.xlsx"   # boş çıkmalı (ignored değil)
git ls-files data/                                 # dosya listelemeli
```
Eğer dosya tracked değilse: `git add "data/Sales Demo Data.xlsx"` → commit → push.

### ❌ PDF Türkçe karakterleri bozuk (ş yerine kare, ı yerine soru işareti)

`fonts/` klasörü deploy'a dahil değil veya dosyalar bozuk.

**Çözüm:**
```powershell
git ls-files fonts/                                # 2 dosya görmeli
ls -la fonts/                                       # her biri ~700KB olmalı
```
Eksikse: `git add fonts/` → commit → push.

### ❌ "You do not have admin permissions on GitHub for this repository"

Streamlit Cloud yanlış GitHub hesabıyla bağlanmış.

**Çözüm:** Sign out → tarayıcıda doğru GitHub hesabına geç → tekrar "Continue with GitHub" ile bağlan.

### ❌ "This file does not exist" (app.py için)

Streamlit Cloud repo'yu okuyamıyor — büyük ihtimalle repo private.

**Çözüm:** GitHub repo Settings → Danger Zone → "Change visibility" → **Public** yap. Veya Streamlit GitHub App'ine repo erişimi ver.

### ❌ Build sırasında timeout

Bundled font (~1.5 MB) git üzerinden çekilirken Streamlit Cloud sınırını aşıyor — nadir görülen durum.

**Çözüm:** Repo'yu shallow clone yerine standart clone yapacak şekilde yenile. Genelde otomatik düzelir; sorun devam ederse Streamlit forum'a bildir.

### ❌ App "Sleeping" durumda

Streamlit Cloud free tier 7 gün etkileşim olmazsa app'i uyutuyor.

**Çözüm:** URL'i aç → "Yes, wake it up" butonuna bas → 30 saniye içinde uyanır.

---

## 6. Güvenlik notları

### .env asla deploy'a girmemeli

- `.env` `.gitignore`'da listelenmiş (line 2)
- `.env.*` (varyantlar) da gitignored (line 3)
- Bu sayede `.env`, `.env.local`, `.env.production` vb. dosyalar git'e hiç giremez
- Streamlit Cloud sadece git'teki dosyaları deploy eder → `.env` orada olmayacak demektir

### Repo'yu zip'leyip paylaşırsan

Eğer repo'yu birine zip olarak gönderirsen `git archive` kullan:

```powershell
git archive --format=zip --output=demo.zip HEAD
```

Bu komut **sadece tracked dosyaları** zip'ler — `.env` gibi gitignored dosyalar dahil olmaz. **Manuel zip yapma**; çünkü filesystem'den zip alırsan `.env` ve `__pycache__` da girer.

### API key gerekirse (gelecekte v15)

Eğer OpenAI API entegrasyonunu açacaksan:

1. Streamlit Cloud sağ alt **"Manage app"** → **Settings** → **Secrets**
2. TOML formatında ekle:
   ```toml
   OPENAI_API_KEY = "sk-..."
   ```
3. Kod tarafında `st.secrets["OPENAI_API_KEY"]` ile oku
4. **`.env`'i deploy'a dahil etme** — Streamlit Secrets kullan

Şu anki MVP'de bu gerekmez; demo tamamen lokal AI-like summary kullanır.

### Sentetik veri kuralı

Repo'da sadece sentetik veri olmalı:
- `data/Sales Demo Data.xlsx` — sentetik
- `test_data/*.xlsx` — sentetik
- `demo_outputs/*` — sentetik veriden üretilmiş

Gerçek müşteri verisi **asla** commit edilmemeli. Müşteri pilotu için on-prem veya geçici workspace kullanılır.

---

## 7. Alternatif platformlar

Streamlit Cloud free tier'ın sınırlamaları (7 gün uyku, public-only, 1 GB RAM) müşteri pilotu için yetersiz kalırsa:

### Render (https://render.com)

- Free tier var, ama uygulama 15 dk inactive olunca uyur
- Custom domain destekler
- Python build pipeline standart
- `requirements.txt` aynen kullanılır
- Start command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

### Railway (https://railway.app)

- Free tier saatlik kredi tabanlı
- Container-based, Docker desteği var
- Streamlit için Procfile veya `railway.json`

### Self-hosted (kendi VPS)

- Hetzner / DigitalOcean / Linode'da 5-10 EUR/ay'lık VPS
- `pip install -r requirements.txt` + `streamlit run app.py` + reverse proxy (Caddy/nginx)
- Müşteri pilotu için en kontrollü seçenek
- KVKK/GDPR uyumu daha kolay konuşulur

### Docker (on-prem müşteri kurulumu)

İleride bir müşteri "kendi sunucumda çalışsın" derse:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
```

Bu yapı `fonts/`, `data/`, kod hepsini içerir. `.env` Docker secret olarak verilir.

---

## Hızlı referans

| Eylem | Komut |
|---|---|
| Lokal test | `streamlit run app.py` |
| Yeni commit + auto deploy | `git push origin main` |
| Manuel reboot | Streamlit Cloud → Manage app → ⋮ → Reboot app |
| Logs incele | Streamlit Cloud → Manage app → Logs |
| Secrets ekle | Manage app → Settings → Secrets |
| Uygulamayı sil | Manage app → ⋮ → Delete app (geri alınamaz) |

İlgili dokümanlar:
- Test senaryoları → [TESTING.md](TESTING.md)
- Müşteri demosu → [DEMO_CHECKLIST.md](DEMO_CHECKLIST.md)
- Proje vizyonu & roadmap → [CLAUDE.md](CLAUDE.md)
- Sürüm geçmişi → [PROJECT_HISTORY.md](PROJECT_HISTORY.md)
