REPORT_TYPE = "sales"
REPORT_LABEL = "Satış / Yönetici Raporu"


REQUIRED_COLUMNS = [
    "Tarih",
    "Müşteri",
    "Satış Temsilcisi",
    "Bölge",
    "Ürün",
    "Satış Tutarı",
    "Durum",
    "Ödeme Durumu",
    "Müşteri Tipi",
    "Not",
]


OPTIONAL_AUTO_FILL_VALUES = {
    "Müşteri Tipi": "Bilinmiyor",
    "Not": "",
}


COLUMN_ALIASES = {
    "Tarih": [
        "Tarih",
        "Satış Tarihi",
        "Fatura Tarihi",
        "Sipariş Tarihi",
        "Date",
    ],
    "Müşteri": [
        "Müşteri",
        "Müşteri Adı",
        "Cari",
        "Cari Adı",
        "Firma",
        "Firma Adı",
        "Customer",
        "Client",
    ],
    "Satış Temsilcisi": [
        "Satış Temsilcisi",
        "Satışçı",
        "Temsilci",
        "Satış Personeli",
        "Sales Rep",
    ],
    "Bölge": [
        "Bölge",
        "Şehir",
        "İl",
        "Lokasyon",
        "Region",
    ],
    "Ürün": [
        "Ürün",
        "Paket",
        "Hizmet",
        "Product",
    ],
    "Satış Tutarı": [
        "Satış Tutarı",
        "Tutar",
        "Net Ciro",
        "Ciro",
        "Gelir",
        "Amount",
        "Sales Amount",
    ],
    "Durum": [
        "Durum",
        "Satış Durumu",
        "Fırsat Durumu",
        "Status",
    ],
    "Ödeme Durumu": [
        "Ödeme Durumu",
        "Tahsilat Durumu",
        "Ödeme",
        "Payment Status",
    ],
    "Müşteri Tipi": [
        "Müşteri Tipi",
        "Segment",
        "Yeni/Mevcut",
        "Customer Type",
    ],
    "Not": [
        "Not",
        "Açıklama",
        "Description",
        "Note",
    ],
}


TEMPLATE_SAMPLE_DATA = {
    "Tarih": ["2026-05-01", "2026-05-02", "2026-05-03"],
    "Müşteri": ["ABC Ltd", "Delta AŞ", "Nova Teknoloji"],
    "Satış Temsilcisi": ["Ayşe", "Mehmet", "Elif"],
    "Bölge": ["İstanbul", "Ankara", "İzmir"],
    "Ürün": ["Paket A", "Paket B", "Paket C"],
    "Satış Tutarı": [45000, 72000, 125000],
    "Durum": ["Kazanıldı", "Beklemede", "Kaybedildi"],
    "Ödeme Durumu": ["Ödendi", "Bekliyor", "Gecikti"],
    "Müşteri Tipi": ["Yeni", "Mevcut", "Mevcut"],
    "Not": ["İlk satış", "Takip edilecek", "Kayıp nedeni analiz edilecek"],
}
