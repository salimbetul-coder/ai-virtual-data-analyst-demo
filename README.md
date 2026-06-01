# AI Virtual Data Analyst

Excel'den 5 dakikada yönetici raporu, veri kalite kontrolü ve aksiyon önerileri.

**Canlı demo:** https://ai-virtual-data-analyst.streamlit.app

BI/data ekibi olmayan KOBİ'ler için tasarlandı. Kullanıcı Excel yükler; sistem satış verisini analiz eder, veri hatalarını ve riskli müşterileri bulur, yönetici diline çevrilmiş bir özet üretir, çıktıları PDF/Markdown/CSV/JSON olarak indirilebilir hale getirir.

---

## Ne yapıyor

- Excel yükleme + kolon doğrulama (standart olmayan kolon adları için eşleştirme ekranı)
- KPI'lar: toplam satış, kazanılan satış, beklemede/kaybedilen sayıları
- Bölge / ürün / satış temsilcisi kırılımları
- Veri kalite problemleri (eksik, hatalı, tutarsız kayıtlar)
- Risk skoru + öncelikli müşteri listesi
- AI-like yönetici yorumu (local, API gerektirmez)
- 6 sayfalık profesyonel PDF rapor (kapak + KPI kartları + tablolar)

---

## Hızlı başlangıç (lokal)

```powershell
pip install -r requirements.txt
streamlit run app.py
```

Tarayıcıda `http://localhost:8501` açılır. Sol panelden örnek şablonu indir veya kendi Excel'ini yükle → "Analiz Et" butonuna bas.

### Komut satırından da çalıştırılabilir

```powershell
python analyze_sales.py          # Excel'i analiz et, output/ klasörüne yaz
python generate_ai_summary.py    # AI yorumu + birleşik raporu üret
python generate_test_data.py     # test_data/ altına sentetik Excel'ler üret
```

---

## Deploy (Streamlit Cloud)

1. https://share.streamlit.io → GitHub ile giriş
2. **New app** → repo seç → branch `main` → main file `app.py`
3. Deploy

Detaylı checklist için [PROJECT_HISTORY.md](PROJECT_HISTORY.md) "v14 — Demo Deploy Hazırlığı" bölümüne bak.

---

## Proje yapısı

```
ai-virtual-data-analyst-demo/
├── app.py                       # Streamlit UI
├── analyze_sales.py             # Analiz motoru + PDF üretimi
├── generate_ai_summary.py       # Yönetici yorumu üretimi (local)
├── generate_ai_summary_api.py   # OpenAI API yolu (varsayılan kapalı)
├── file_validator.py            # Kolon doğrulama + eşleştirme + hafıza
├── app_utils.py                 # Dosya okuma, indirme yardımcıları
├── generate_test_data.py        # Sentetik test Excel üretici
├── report_schemas/
│   └── sales.py                 # Satış raporu kolon şeması ve aliasları
├── data/
│   └── Sales Demo Data.xlsx     # Bundled sentetik demo veri
├── test_data/                   # Clean / dirty / large test dosyaları
├── demo_outputs/                # Donmuş showcase çıktıları
├── fonts/                       # DejaVu Sans (PDF için, Unicode/Türkçe)
├── .streamlit/config.toml       # Kurumsal light tema
├── requirements.txt
└── PROJECT_HISTORY.md           # v1 → v14 sürüm geçmişi
```

---

## Güvenlik & paylaşım

- `.env` **asla** commit edilmez, **asla** paylaşılan zip'e konmaz. `.gitignore` bunu zorunlu kılar.
- Repoyu zip'leyip paylaşacaksan zip içeriğini açıp `.env`'in olmadığını manuel doğrula.
- Demo verisi (`data/`, `test_data/`) tamamen sentetiktir; gerçek müşteri verisi commit edilmemelidir.
- OpenAI API entegrasyonu **kapalı**. Demo tamamen lokal AI-like summary kullanır, internet erişimi gerektirmez.
- Yeni anahtar eklemek istersen `.env.example` dosyasını kopyala → `.env` yap → değerini doldur.

---

## Teknolojiler

Python 3.12 · Streamlit · pandas · openpyxl · fpdf2 · DejaVu Sans

---

## Daha fazla

- **Deploy rehberi (Streamlit Cloud, adım adım):** [DEPLOYMENT.md](DEPLOYMENT.md)
- **Test rehberi (3 test verisi, beklenen metrikler, UI akışı):** [TESTING.md](TESTING.md)
- **Müşteri/demo sunumu checklist'i:** [DEMO_CHECKLIST.md](DEMO_CHECKLIST.md)
- **Sürüm geçmişi (v1 → v14):** [PROJECT_HISTORY.md](PROJECT_HISTORY.md)
- **Proje vizyonu, çalışma kuralları, roadmap:** [CLAUDE.md](CLAUDE.md)
