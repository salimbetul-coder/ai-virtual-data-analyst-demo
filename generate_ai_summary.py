from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

INPUT_JSON = OUTPUT_DIR / "analysis_result_v4.json"
INPUT_REPORT = OUTPUT_DIR / "generated_report_v4.md"

PROMPT_OUTPUT = OUTPUT_DIR / "ai_prompt_v5.txt"
AI_SUMMARY_OUTPUT = OUTPUT_DIR / "generated_ai_summary_v5.md"
FINAL_REPORT_OUTPUT = OUTPUT_DIR / "generated_report_v5.md"


RISK_KEYWORDS = [
    "Anormal yüksek satış",
    "Negatif satış tutarı",
    "Durum/ödeme tutarsızlığı",
    "Eksik satış tutarı",
    "Hatalı tarih",
    "Geciken ödeme",
]


def load_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"JSON dosyası bulunamadı: {path}")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_text(path: Path) -> str:
    if not path.exists():
        return ""

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def build_ai_prompt(analysis_result: dict) -> str:
    return f"""
Sen bir şirket yöneticisine rapor yorumlayan senior data analyst gibi davran.

Aşağıdaki JSON, Python analiz motoru tarafından üretilmiş güvenilir hesaplama sonucudur.
Sayıları değiştirme, uydurma metrik ekleme, olmayan veriyi varmış gibi gösterme.

Görevin:
1. Yöneticiye sade ve profesyonel bir özet yaz.
2. Veri kalitesi risklerini açıkla.
3. Satış performansını yorumla.
4. Riskli müşteriler için önceliklendirilmiş aksiyon öner.
5. Sonuçta kısa bir karar destek yorumu ver.

Önemli kurallar:
- Riskli müşteri yorumunda Risk Skoru ve Öncelik alanlarını dikkate al.
- En yüksek risk skoruna sahip müşterileri önce yaz.
- JSON içinde olmayan müşteri veya risk tipi uydurma.
- Anormal yüksek satış yoksa varmış gibi söyleme.
- Sayıları değiştirme.

Ton:
- Yönetici diliyle yaz.
- Teknik terimleri azalt.
- Net, kısa ve aksiyon odaklı ol.
- Gereksiz uzun yazma.
- Uydurma tahmin yapma.

Beklenen çıktı formatı:

# AI Yönetici Yorumu

## 1. Kısa Yönetici Özeti

## 2. Dikkat Edilmesi Gereken Ana Riskler

## 3. Satış Performansı Yorumu

## 4. Öncelikli Aksiyon Planı

## 5. Karar Destek Notu

JSON:
{json.dumps(analysis_result, ensure_ascii=False, indent=2)}
""".strip()


def get_numeric_score(customer: dict) -> int:
    try:
        return int(customer.get("Risk Skoru", 0) or 0)
    except (ValueError, TypeError):
        return 0


def sort_risk_customers_by_priority(risk_customers: list) -> list:
    return sorted(
        risk_customers,
        key=lambda customer: (
            -get_numeric_score(customer),
            str(customer.get("Müşteri", "")),
        ),
    )


def get_outlier_customers(risk_customers: list) -> list:
    customers = []

    for customer in risk_customers:
        risk_type = str(customer.get("Risk Tipi", ""))
        customer_name = str(customer.get("Müşteri", "")).strip()

        if customer_name and "Anormal yüksek satış" in risk_type:
            customers.append(customer_name)

    return customers


def get_outlier_note(risk_customers: list) -> str:
    outlier_customers = get_outlier_customers(risk_customers)

    if outlier_customers:
        customer_text = ", ".join(outlier_customers[:3])

        return (
            f"Ancak **{customer_text}** gibi anormal yüksek satış içeren kayıtlar "
            "toplam performansı şişiriyor olabilir. Bu nedenle yüksek tutarlı satışlar ayrıca doğrulanmalıdır."
        )

    return (
        "Bu olumlu bir sinyal olabilir. Yine de yüksek tutarlı satışların toplam performansı "
        "tek başına domine edip etmediği ayrıca kontrol edilmelidir."
    )


def get_risk_category_summary(risk_customers: list) -> str:
    categories = []

    for keyword in RISK_KEYWORDS:
        if any(keyword in str(customer.get("Risk Tipi", "")) for customer in risk_customers):
            categories.append(keyword.lower())

    if not categories:
        return "Bu veri setinde kritik risk kategorisi bulunmamıştır."

    return "Bu veri setinde öne çıkan riskler; " + ", ".join(categories) + " kayıtlarıdır."


def generate_local_ai_like_summary(analysis_result: dict) -> str:
    summary = analysis_result["summary"]
    data_quality = analysis_result["data_quality"]
    risks = analysis_result["risks"]
    breakdowns = analysis_result["sales_breakdowns"]
    recommendations = analysis_result["recommendations"]

    total_sales = summary["total_sales_formatted"]
    won_sales = summary["won_sales_total_formatted"]
    pending_count = summary["pending_sales_count"]
    lost_count = summary["lost_sales_count"]
    top_region = summary["top_region"]
    top_product = summary["top_product"]
    top_sales_rep = summary["top_sales_rep"]

    issue_count = data_quality["issue_count"]
    risk_count = risks["risk_customer_count"]

    risk_customers = risks.get("customers", [])
    risk_customers = sort_risk_customers_by_priority(risk_customers)

    top_risks_text = []

    for customer in risk_customers[:5]:
        customer_name = customer.get("Müşteri", "Müşteri adı eksik")
        risk_type = customer.get("Risk Tipi", "Risk tipi yok")
        action = customer.get("Önerilen Aksiyon", "Aksiyon önerisi yok")
        priority = customer.get("Öncelik", "Öncelik yok")
        score = customer.get("Risk Skoru", "-")

        top_risks_text.append(
            f"- **{customer_name}** ({priority}, skor: {score}): {risk_type} — {action}"
        )

    if not top_risks_text:
        top_risks_text.append("- Riskli müşteri bulunmamaktadır.")

    region_lines = []

    for item in breakdowns["by_region"][:3]:
        region_lines.append(
            f"- **{item['region']}**: {item['sales_amount_formatted']}"
        )

    product_lines = []

    for item in breakdowns["by_product"][:3]:
        product_lines.append(
            f"- **{item['product']}**: {item['sales_amount_formatted']}"
        )

    recommendation_lines = []

    for index, recommendation in enumerate(recommendations, start=1):
        recommendation_lines.append(f"{index}. {recommendation}")

    risk_category_summary = get_risk_category_summary(risk_customers)
    outlier_note = get_outlier_note(risk_customers)

    return f"""# AI Yönetici Yorumu

## 1. Kısa Yönetici Özeti

Bu rapora göre toplam satış tutarı **{total_sales}**, kazanılan satış toplamı ise **{won_sales}** olarak hesaplanmıştır. Satış hacminde **{top_region}** bölgesi, ürün bazında **{top_product}**, satış temsilcisi bazında ise **{top_sales_rep}** öne çıkmaktadır.

Ancak raporda **{issue_count} veri kalite problemi** ve **{risk_count} riskli müşteri kaydı** bulunduğu için bu sonuçlar doğrudan nihai karar için kullanılmamalıdır. Önce veri temizliği ve riskli kayıtların kontrolü yapılmalıdır.

## 2. Dikkat Edilmesi Gereken Ana Riskler

{risk_category_summary} Bu problemler hem toplam satış rakamını hem de bölge/temsilci performansını etkileyebilir.

Öncelikli riskli müşteriler:

{chr(10).join(top_risks_text)}

## 3. Satış Performansı Yorumu

Bölge bazında ilk üç satış hacmi:

{chr(10).join(region_lines)}

Ürün bazında satış hacmi:

{chr(10).join(product_lines)}

Satışın büyük kısmı **{top_product}** üzerinde yoğunlaşmış görünüyor. {outlier_note}

Beklemede olan **{pending_count} satış** için hızlı takip yapılması, kısa vadede satışa dönüş potansiyeli yaratabilir. Kaybedilen **{lost_count} satış** için de kayıp nedeni analizi standart hale getirilmelidir.

## 4. Öncelikli Aksiyon Planı

{chr(10).join(recommendation_lines)}

## 5. Karar Destek Notu

Bu rapor, satış performansının genel olarak güçlü göründüğünü fakat karar almadan önce veri kalitesi kontrolünün zorunlu olduğunu gösteriyor. Yönetici için en doğru yaklaşım; önce hatalı/eksik kayıtları düzeltmek, ardından yüksek öncelikli riskli müşterileri kontrol etmek, geciken ödemeleri takip etmek ve sonrasında satış performansını yeniden değerlendirmektir.
"""


def generate_ai_summary():
    analysis_result = load_json(INPUT_JSON)
    existing_report = load_text(INPUT_REPORT)

    ai_prompt = build_ai_prompt(analysis_result)
    ai_summary = generate_local_ai_like_summary(analysis_result)

    OUTPUT_DIR.mkdir(exist_ok=True)

    with open(PROMPT_OUTPUT, "w", encoding="utf-8") as file:
        file.write(ai_prompt)

    with open(AI_SUMMARY_OUTPUT, "w", encoding="utf-8") as file:
        file.write(ai_summary)

    final_report = f"""{ai_summary}

---

# Teknik Analiz Raporu

{existing_report}
"""

    with open(FINAL_REPORT_OUTPUT, "w", encoding="utf-8") as file:
        file.write(final_report)

    print("")
    print("v10.3 AI yorum katmanı risk skoru uyumlu şekilde oluşturuldu.")
    print(f"AI prompt dosyası: {PROMPT_OUTPUT}")
    print(f"AI yorum dosyası: {AI_SUMMARY_OUTPUT}")
    print(f"Birleşik v5 rapor dosyası: {FINAL_REPORT_OUTPUT}")

    return {
        "prompt_path": str(PROMPT_OUTPUT),
        "ai_summary_path": str(AI_SUMMARY_OUTPUT),
        "final_report_path": str(FINAL_REPORT_OUTPUT),
    }


def main():
    return generate_ai_summary()


if __name__ == "__main__":
    main()
