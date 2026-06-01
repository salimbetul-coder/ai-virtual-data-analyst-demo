from pathlib import Path
import random
from datetime import datetime, timedelta

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
TEST_DATA_DIR = BASE_DIR / "test_data"


COLUMNS = [
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


CUSTOMERS = [
    "Atlas Holding",
    "Delta İnşaat",
    "Mavi Lojistik",
    "Pera Tekstil",
    "Ege Kozmetik",
    "Kare Mobilya",
    "Zen Yapı",
    "Star Medya",
    "Nova Teknoloji",
    "Lima Gıda",
    "Orion Yazılım",
    "Vera Danışmanlık",
    "Akdeniz Turizm",
    "Bora Enerji",
    "İnci Sağlık",
    "Rota Eğitim",
    "Mira Perakende",
    "Eksen Otomotiv",
    "Safir Medikal",
    "Kuzey Market",
]

SALES_REPS = ["Ayşe", "Mehmet", "Elif", "Can", "Zeynep", "Burak"]
REGIONS = ["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya", "Konya"]
PRODUCTS = ["Paket A", "Paket B", "Paket C"]
STATUSES = ["Kazanıldı", "Beklemede", "Kaybedildi"]
PAYMENT_STATUSES = ["Ödendi", "Bekliyor"]
CUSTOMER_TYPES = ["Yeni", "Mevcut"]


def random_date(start_date: datetime, days: int) -> str:
    date = start_date + timedelta(days=random.randint(0, days))
    return date.strftime("%Y-%m-%d")


def save_excel(df: pd.DataFrame, file_path: Path):
    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Sales Demo Data")


def create_clean_sales_data():
    rows = []
    start_date = datetime(2026, 5, 1)

    for index in range(60):
        status = random.choice(STATUSES)

        if status == "Kaybedildi":
            payment_status = "Bekliyor"
        else:
            payment_status = random.choice(PAYMENT_STATUSES)

        rows.append(
            {
                "Tarih": random_date(start_date, 30),
                "Müşteri": random.choice(CUSTOMERS),
                "Satış Temsilcisi": random.choice(SALES_REPS),
                "Bölge": random.choice(REGIONS),
                "Ürün": random.choice(PRODUCTS),
                "Satış Tutarı": random.randint(15000, 180000),
                "Durum": status,
                "Ödeme Durumu": payment_status,
                "Müşteri Tipi": random.choice(CUSTOMER_TYPES),
                "Not": "Temiz test kaydı",
            }
        )

    return pd.DataFrame(rows, columns=COLUMNS)


def create_dirty_sales_data():
    rows = [
        {
            "Tarih": "2026-05-01",
            "Müşteri": "Atlas Holding",
            "Satış Temsilcisi": "Ayşe",
            "Bölge": "İstanbul",
            "Ürün": "Paket C",
            "Satış Tutarı": 950000,
            "Durum": "Kazanıldı",
            "Ödeme Durumu": "Ödendi",
            "Müşteri Tipi": "Mevcut",
            "Not": "Anormal yüksek satış kontrol edilmeli",
        },
        {
            "Tarih": "2026-05-03",
            "Müşteri": "Delta İnşaat",
            "Satış Temsilcisi": "Mehmet",
            "Bölge": "Ankara",
            "Ürün": "Paket B",
            "Satış Tutarı": 72000,
            "Durum": "Kazanıldı",
            "Ödeme Durumu": "Gecikti",
            "Müşteri Tipi": "Mevcut",
            "Not": "Tahsilat gecikmiş",
        },
        {
            "Tarih": "2026-13-02",
            "Müşteri": "Kare Mobilya",
            "Satış Temsilcisi": "Elif",
            "Bölge": "Bursa",
            "Ürün": "Paket A",
            "Satış Tutarı": 43000,
            "Durum": "Beklemede",
            "Ödeme Durumu": "Gecikti",
            "Müşteri Tipi": "Yeni",
            "Not": "Hatalı tarih ve geciken ödeme",
        },
        {
            "Tarih": "2026-05-07",
            "Müşteri": "Pera Tekstil",
            "Satış Temsilcisi": "Can",
            "Bölge": "İzmir",
            "Ürün": "Paket C",
            "Satış Tutarı": None,
            "Durum": "Kazanıldı",
            "Ödeme Durumu": "Bekliyor",
            "Müşteri Tipi": "Mevcut",
            "Not": "Satış tutarı eksik",
        },
        {
            "Tarih": "2026-05-09",
            "Müşteri": "Ege Kozmetik",
            "Satış Temsilcisi": "Zeynep",
            "Bölge": "Antalya",
            "Ürün": "Paket A",
            "Satış Tutarı": -18000,
            "Durum": "Kazanıldı",
            "Ödeme Durumu": "Ödendi",
            "Müşteri Tipi": "Yeni",
            "Not": "Negatif satış tutarı",
        },
        {
            "Tarih": "2026-05-11",
            "Müşteri": "Zen Yapı",
            "Satış Temsilcisi": "Burak",
            "Bölge": None,
            "Ürün": "Paket B",
            "Satış Tutarı": 38000,
            "Durum": "Beklemede",
            "Ödeme Durumu": "Bekliyor",
            "Müşteri Tipi": "Yeni",
            "Not": "Bölge eksik",
        },
        {
            "Tarih": "2026-05-13",
            "Müşteri": "Star Medya",
            "Satış Temsilcisi": None,
            "Bölge": "İstanbul",
            "Ürün": "Paket A",
            "Satış Tutarı": 29000,
            "Durum": "Beklemede",
            "Ödeme Durumu": "Bekliyor",
            "Müşteri Tipi": "Mevcut",
            "Not": "Satış temsilcisi eksik",
        },
        {
            "Tarih": "2026-05-15",
            "Müşteri": "Doruk Gıda",
            "Satış Temsilcisi": "Ayşe",
            "Bölge": "İstanbul",
            "Ürün": "Paket B",
            "Satış Tutarı": 58000,
            "Durum": "Kaybedildi",
            "Ödeme Durumu": "Ödendi",
            "Müşteri Tipi": "Mevcut",
            "Not": "Kaybedildi ama ödeme alınmış görünüyor",
        },
        {
            "Tarih": "2026-05-18",
            "Müşteri": "Kuzey Market",
            "Satış Temsilcisi": "Mehmet",
            "Bölge": "Konya",
            "Ürün": "Paket C",
            "Satış Tutarı": 64000,
            "Durum": "Tamamlandı",
            "Ödeme Durumu": "Ödendi",
            "Müşteri Tipi": "Yeni",
            "Not": "Standart dışı durum değeri",
        },
    ]

    return pd.DataFrame(rows, columns=COLUMNS)


def create_large_sales_data(row_count: int = 500):
    rows = []
    start_date = datetime(2026, 1, 1)

    for index in range(row_count):
        status = random.choice(STATUSES)

        if status == "Kaybedildi":
            payment_status = random.choice(["Bekliyor", "Gecikti"])
        elif status == "Beklemede":
            payment_status = random.choice(["Bekliyor", "Gecikti"])
        else:
            payment_status = random.choice(["Ödendi", "Bekliyor", "Gecikti"])

        amount = random.randint(10000, 250000)

        row = {
            "Tarih": random_date(start_date, 150),
            "Müşteri": random.choice(CUSTOMERS),
            "Satış Temsilcisi": random.choice(SALES_REPS),
            "Bölge": random.choice(REGIONS),
            "Ürün": random.choice(PRODUCTS),
            "Satış Tutarı": amount,
            "Durum": status,
            "Ödeme Durumu": payment_status,
            "Müşteri Tipi": random.choice(CUSTOMER_TYPES),
            "Not": "Büyük veri test kaydı",
        }

        rows.append(row)

    # Büyük dataset içine bilinçli birkaç problem ekliyoruz.
    rows[15]["Satış Tutarı"] = None
    rows[42]["Bölge"] = None
    rows[78]["Satış Temsilcisi"] = None
    rows[120]["Tarih"] = "2026-14-20"
    rows[155]["Satış Tutarı"] = -25000
    rows[210]["Durum"] = "Tamamlandı"
    rows[260]["Durum"] = "Kaybedildi"
    rows[260]["Ödeme Durumu"] = "Ödendi"
    rows[320]["Satış Tutarı"] = 1500000
    rows[321]["Müşteri"] = "Mega Grup"
    rows[321]["Ödeme Durumu"] = "Gecikti"

    return pd.DataFrame(rows, columns=COLUMNS)


def main():
    TEST_DATA_DIR.mkdir(exist_ok=True)

    clean_df = create_clean_sales_data()
    dirty_df = create_dirty_sales_data()
    large_df = create_large_sales_data()

    clean_path = TEST_DATA_DIR / "clean_sales_data.xlsx"
    dirty_path = TEST_DATA_DIR / "dirty_sales_data.xlsx"
    large_path = TEST_DATA_DIR / "large_sales_data.xlsx"

    save_excel(clean_df, clean_path)
    save_excel(dirty_df, dirty_path)
    save_excel(large_df, large_path)

    print("")
    print("Test data dosyaları oluşturuldu:")
    print(f"- {clean_path}")
    print(f"- {dirty_path}")
    print(f"- {large_path}")


if __name__ == "__main__":
    main()