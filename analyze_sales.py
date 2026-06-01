from datetime import date
from pathlib import Path
import json

import pandas as pd
from fpdf import FPDF


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"


PDF_BRAND_LABEL = "AI Virtual Data Analyst"
PDF_BRAND_TAGLINE = "AI Virtual Data Team — Excel'den 5 dakikada yönetici raporu"
PDF_COLOR_PRIMARY = (15, 30, 60)
PDF_COLOR_ACCENT = (60, 110, 200)
PDF_COLOR_SUCCESS = (45, 120, 80)
PDF_COLOR_WARN = (210, 130, 25)
PDF_COLOR_DANGER = (190, 50, 50)
PDF_COLOR_TEXT = (30, 30, 30)
PDF_COLOR_MUTED = (130, 130, 130)
PDF_COLOR_DIVIDER = (220, 222, 228)
PDF_COLOR_HAIRLINE = (200, 205, 215)
PDF_COLOR_HIGHLIGHT_BG = (248, 250, 253)
PDF_PRIORITY_COLORS = {
    "Yüksek": PDF_COLOR_DANGER,
    "Orta": PDF_COLOR_WARN,
    "Düşük": PDF_COLOR_SUCCESS,
}


POSSIBLE_FILES = [
    DATA_DIR / "Sales Demo Data.xlsx",
    DATA_DIR / "sales_demo_data.xlsx",
]


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


ALLOWED_STATUSES = {"kazanıldı", "beklemede", "kaybedildi"}


def find_excel_file() -> Path:
    for file_path in POSSIBLE_FILES:
        if file_path.exists():
            return file_path

    excel_files = list(DATA_DIR.glob("*.xlsx"))
    if excel_files:
        return excel_files[0]

    raise FileNotFoundError("data klasöründe .xlsx dosyası bulunamadı.")


def safe_text(value) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip()


def clean_amount(value):
    if pd.isna(value):
        return pd.NA

    if isinstance(value, (int, float)):
        return float(value)

    text = str(value).strip()
    text = text.replace("TL", "").replace("₺", "").strip()
    text = text.replace(".", "").replace(",", ".")

    try:
        return float(text)
    except ValueError:
        return pd.NA


def format_tl(value) -> str:
    if pd.isna(value):
        return "0 TL"
    return f"{value:,.0f} TL".replace(",", ".")


def display_value(value) -> str:
    if pd.isna(value):
        return "Eksik değer"

    if isinstance(value, (int, float)):
        if float(value).is_integer():
            return f"{int(value):,}".replace(",", ".")
        return f"{float(value):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    text = str(value).strip()

    if text.lower() == "nan" or text == "":
        return "Eksik değer"

    return text


def dataframe_to_records(df: pd.DataFrame):
    if df.empty:
        return []

    cleaned_df = df.copy().astype(object)
    cleaned_df = cleaned_df.where(pd.notna(cleaned_df), None)

    return cleaned_df.to_dict(orient="records")


def series_to_records(series, name_key, value_key, missing_label):
    records = []

    for name, value in series.items():
        clean_name = safe_text(name) or missing_label

        records.append(
            {
                name_key: clean_name,
                value_key: float(value),
                f"{value_key}_formatted": format_tl(value),
            }
        )

    return records


class ReportPDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font_regular = "Helvetica"
        self.font_bold = "Helvetica"
        self.show_chrome = False

    def header(self):
        if not self.show_chrome:
            return
        self.set_y(9)
        self.set_font(self.font_bold, "B", 8)
        self.set_text_color(*PDF_COLOR_PRIMARY)
        self.cell(self.epw / 2, 4, PDF_BRAND_LABEL, align="L")
        self.set_font(self.font_regular, "", 8)
        self.set_text_color(*PDF_COLOR_MUTED)
        today_str = date.today().strftime("%d.%m.%Y")
        self.cell(self.epw / 2, 4, f"Yönetici Raporu · {today_str}", align="R")
        self.set_draw_color(*PDF_COLOR_HAIRLINE)
        self.set_line_width(0.2)
        self.line(self.l_margin, 15, self.w - self.r_margin, 15)
        self.set_y(20)
        self.set_text_color(*PDF_COLOR_TEXT)

    def footer(self):
        if not self.show_chrome:
            return
        self.set_y(-14)
        self.set_draw_color(*PDF_COLOR_HAIRLINE)
        self.set_line_width(0.2)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.set_y(-11)
        self.set_font(self.font_regular, "", 8)
        self.set_text_color(*PDF_COLOR_MUTED)
        self.cell(self.epw / 2, 5, PDF_BRAND_TAGLINE, align="L")
        self.cell(self.epw / 2, 5, f"{self.page_no()}", align="R")
        self.set_text_color(*PDF_COLOR_TEXT)


def _setup_pdf_fonts(pdf: ReportPDF) -> None:
    bundled_regular = BASE_DIR / "fonts" / "DejaVuSans.ttf"
    bundled_bold = BASE_DIR / "fonts" / "DejaVuSans-Bold.ttf"

    if bundled_regular.exists() and bundled_bold.exists():
        pdf.add_font("ReportFont", "", str(bundled_regular))
        pdf.add_font("ReportFont", "B", str(bundled_bold))
        pdf.font_regular = "ReportFont"
        pdf.font_bold = "ReportFont"
        return

    windows_regular = Path(r"C:\Windows\Fonts\arial.ttf")
    windows_bold = Path(r"C:\Windows\Fonts\arialbd.ttf")
    if windows_regular.exists() and windows_bold.exists():
        pdf.add_font("ReportFont", "", str(windows_regular))
        pdf.add_font("ReportFont", "B", str(windows_bold))
        pdf.font_regular = "ReportFont"
        pdf.font_bold = "ReportFont"


def _draw_cover_page(pdf: ReportPDF, source_file: str) -> None:
    pdf.show_chrome = False
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    pdf.set_fill_color(*PDF_COLOR_PRIMARY)
    pdf.rect(0, 0, 10, pdf.h, "F")
    pdf.set_fill_color(*PDF_COLOR_ACCENT)
    pdf.rect(10, 0, 2, pdf.h, "F")

    pdf.set_xy(pdf.l_margin + 10, 60)
    pdf.set_text_color(*PDF_COLOR_ACCENT)
    pdf.set_font(pdf.font_bold, "B", 11)
    pdf.cell(0, 6, "YÖNETİCİ RAPORU", new_x="LMARGIN", new_y="NEXT")

    pdf.set_x(pdf.l_margin + 10)
    pdf.set_text_color(*PDF_COLOR_PRIMARY)
    pdf.set_font(pdf.font_bold, "B", 34)
    pdf.cell(0, 18, "Satış Performansı", new_x="LMARGIN", new_y="NEXT")

    pdf.set_x(pdf.l_margin + 10)
    pdf.set_text_color(*PDF_COLOR_PRIMARY)
    pdf.set_font(pdf.font_regular, "", 14)
    pdf.cell(0, 8, "& Veri Kalite Analizi", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(6)
    pdf.set_x(pdf.l_margin + 10)
    pdf.set_draw_color(*PDF_COLOR_HAIRLINE)
    pdf.set_line_width(0.3)
    pdf.line(
        pdf.l_margin + 10,
        pdf.get_y(),
        pdf.l_margin + 60,
        pdf.get_y(),
    )

    pdf.ln(8)
    pdf.set_x(pdf.l_margin + 10)
    pdf.set_text_color(*PDF_COLOR_MUTED)
    pdf.set_font(pdf.font_regular, "", 10)
    pdf.cell(0, 6, "Hazırlayan:", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(pdf.l_margin + 10)
    pdf.set_text_color(*PDF_COLOR_TEXT)
    pdf.set_font(pdf.font_bold, "B", 12)
    pdf.cell(0, 7, PDF_BRAND_LABEL, new_x="LMARGIN", new_y="NEXT")

    pdf.set_y(pdf.h - 65)
    pdf.set_x(pdf.l_margin + 10)
    pdf.set_draw_color(*PDF_COLOR_HAIRLINE)
    pdf.line(
        pdf.l_margin + 10,
        pdf.get_y(),
        pdf.w - pdf.r_margin,
        pdf.get_y(),
    )

    pdf.ln(4)
    today_str = date.today().strftime("%d.%m.%Y")
    info_pairs = [
        ("RAPOR TARİHİ", today_str),
        ("KAYNAK DOSYA", source_file),
        ("RAPOR TÜRÜ", "Satış / Yönetici Raporu"),
    ]
    for label, value in info_pairs:
        pdf.set_x(pdf.l_margin + 10)
        pdf.set_text_color(*PDF_COLOR_MUTED)
        pdf.set_font(pdf.font_regular, "", 8)
        pdf.cell(40, 5, label)
        pdf.set_text_color(*PDF_COLOR_TEXT)
        pdf.set_font(pdf.font_bold, "B", 10)
        pdf.cell(0, 5, str(value), new_x="LMARGIN", new_y="NEXT")

    pdf.set_y(pdf.h - 22)
    pdf.set_x(pdf.l_margin + 10)
    pdf.set_text_color(*PDF_COLOR_MUTED)
    pdf.set_font(pdf.font_regular, "", 8)
    pdf.cell(0, 5, PDF_BRAND_TAGLINE, align="L")

    pdf.set_text_color(*PDF_COLOR_TEXT)
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.show_chrome = True


def _draw_section_title(pdf: ReportPDF, title: str, eyebrow: str = None) -> None:
    pdf.ln(4)
    y_start = pdf.get_y()

    pdf.set_fill_color(*PDF_COLOR_ACCENT)
    pdf.rect(pdf.l_margin, y_start + 1, 1.4, 9, "F")

    pdf.set_xy(pdf.l_margin + 4, y_start)
    if eyebrow:
        pdf.set_text_color(*PDF_COLOR_ACCENT)
        pdf.set_font(pdf.font_bold, "B", 8)
        pdf.cell(0, 4, eyebrow.upper(), new_x="LMARGIN", new_y="NEXT")
        pdf.set_x(pdf.l_margin + 4)

    pdf.set_text_color(*PDF_COLOR_PRIMARY)
    pdf.set_font(pdf.font_bold, "B", 15)
    pdf.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")

    pdf.set_draw_color(*PDF_COLOR_HAIRLINE)
    pdf.set_line_width(0.2)
    y = pdf.get_y() + 1
    pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)

    pdf.set_text_color(*PDF_COLOR_TEXT)
    pdf.ln(5)


def _draw_kpi_cards(pdf: ReportPDF, summary: dict, data_quality: dict, risks: dict) -> None:
    kpis = [
        (
            "TOPLAM SATIŞ",
            summary.get("total_sales_formatted", "-"),
            "Ham satış verisine göre",
            PDF_COLOR_PRIMARY,
        ),
        (
            "KAZANILAN SATIŞ",
            summary.get("won_sales_total_formatted", "-"),
            "Kazanıldı durumundaki kayıtlar",
            PDF_COLOR_SUCCESS,
        ),
        (
            "VERİ KALİTE PROBLEMİ",
            str(data_quality.get("issue_count", "-")),
            "Eksik, hatalı, tutarsız kayıt",
            PDF_COLOR_WARN,
        ),
        (
            "RİSKLİ MÜŞTERİ",
            str(risks.get("risk_customer_count", "-")),
            "Takip gerektiren müşteri",
            PDF_COLOR_DANGER,
        ),
    ]

    gap = 5
    card_w = (pdf.epw - gap) / 2
    card_h = 28
    y0 = pdf.get_y()

    for index, (label, value, subtitle, color) in enumerate(kpis):
        row = index // 2
        col = index % 2
        x = pdf.l_margin + col * (card_w + gap)
        y = y0 + row * (card_h + gap)

        pdf.set_fill_color(255, 255, 255)
        pdf.set_draw_color(*PDF_COLOR_DIVIDER)
        pdf.set_line_width(0.2)
        pdf.rect(x, y, card_w, card_h, "DF")

        pdf.set_fill_color(*color)
        pdf.rect(x, y, card_w, 1.6, "F")

        pdf.set_xy(x + 5, y + 4)
        pdf.set_text_color(*PDF_COLOR_MUTED)
        pdf.set_font(pdf.font_bold, "B", 7.5)
        pdf.cell(card_w - 10, 4, label)

        pdf.set_xy(x + 5, y + 10)
        pdf.set_text_color(*color)
        pdf.set_font(pdf.font_bold, "B", 18)
        pdf.cell(card_w - 10, 10, value)

        pdf.set_xy(x + 5, y + 21)
        pdf.set_text_color(*PDF_COLOR_MUTED)
        pdf.set_font(pdf.font_regular, "", 8)
        pdf.cell(card_w - 10, 4, subtitle)

    pdf.set_y(y0 + 2 * (card_h + gap))
    pdf.set_text_color(*PDF_COLOR_TEXT)


def _draw_highlights(pdf: ReportPDF, summary: dict) -> None:
    items = [
        ("EN GÜÇLÜ BÖLGE", summary.get("top_region", "-")),
        ("EN GÜÇLÜ ÜRÜN", summary.get("top_product", "-")),
        ("EN GÜÇLÜ TEMSİLCİ", summary.get("top_sales_rep", "-")),
    ]
    pdf.ln(3)
    y0 = pdf.get_y()
    gap = 4
    box_w = (pdf.epw - 2 * gap) / 3
    box_h = 18

    for index, (label, value) in enumerate(items):
        x = pdf.l_margin + index * (box_w + gap)
        pdf.set_fill_color(*PDF_COLOR_HIGHLIGHT_BG)
        pdf.set_draw_color(*PDF_COLOR_DIVIDER)
        pdf.set_line_width(0.2)
        pdf.rect(x, y0, box_w, box_h, "DF")

        pdf.set_xy(x + 4, y0 + 3)
        pdf.set_text_color(*PDF_COLOR_MUTED)
        pdf.set_font(pdf.font_bold, "B", 7.5)
        pdf.cell(box_w - 8, 4, label)

        pdf.set_xy(x + 4, y0 + 9)
        pdf.set_text_color(*PDF_COLOR_PRIMARY)
        pdf.set_font(pdf.font_bold, "B", 13)
        pdf.cell(box_w - 8, 7, str(value))

    pdf.set_y(y0 + box_h)
    pdf.set_text_color(*PDF_COLOR_TEXT)


def _draw_executive_paragraph(pdf: ReportPDF, summary: dict, data_quality: dict, risks: dict) -> None:
    total = summary.get("total_sales_formatted", "-")
    won = summary.get("won_sales_total_formatted", "-")
    issues = data_quality.get("issue_count", 0)
    risk_count = risks.get("risk_customer_count", 0)

    paragraph = (
        f"Bu raporda toplam {total} satış hacmi tespit edildi; bunun {won} kısmı kazanılan "
        f"satış olarak gerçekleşti. Aynı zamanda {issues} veri kalite problemi ve {risk_count} "
        "riskli müşteri kaydı bulundu. Karar verilmeden önce veri kalitesi kontrolleri "
        "tamamlanmalı, yüksek öncelikli riskli müşteriler doğrulanmalı, geciken ödemeler için "
        "tahsilat takibi başlatılmalıdır."
    )

    pdf.ln(3)
    y0 = pdf.get_y()

    pdf.set_fill_color(*PDF_COLOR_ACCENT)
    pdf.rect(pdf.l_margin, y0 + 1, 1.2, 25, "F")

    pdf.set_xy(pdf.l_margin + 5, y0)
    pdf.set_font(pdf.font_regular, "", 10.5)
    pdf.set_text_color(*PDF_COLOR_TEXT)
    pdf.multi_cell(w=pdf.epw - 5, h=6, text=paragraph)


def _is_muted_row(row) -> bool:
    if not row:
        return False
    return "eksik" in str(row[0]).lower()


def _draw_table_header(pdf: ReportPDF, headers: list, col_widths: list, aligns: list) -> None:
    line_h = 7
    pdf.set_font(pdf.font_bold, "B", 8)
    pdf.set_text_color(*PDF_COLOR_MUTED)

    for header, width, align in zip(headers, col_widths, aligns):
        pdf.cell(width, line_h, str(header).upper(), border=0, align=align)
    pdf.ln(line_h)

    pdf.set_draw_color(*PDF_COLOR_PRIMARY)
    pdf.set_line_width(0.4)
    y_rule = pdf.get_y() - 0.5
    pdf.line(pdf.l_margin, y_rule, pdf.l_margin + sum(col_widths), y_rule)
    pdf.set_line_width(0.2)
    pdf.set_text_color(*PDF_COLOR_TEXT)


def _draw_table(
    pdf: ReportPDF,
    headers: list,
    rows: list,
    col_widths: list,
    aligns: list = None,
    row_colors=None,
    use_priority_pill: bool = False,
) -> None:
    if aligns is None:
        aligns = ["L"] * len(headers)

    if not rows:
        pdf.set_font(pdf.font_regular, "", 10)
        pdf.set_text_color(*PDF_COLOR_MUTED)
        pdf.multi_cell(w=pdf.epw, h=6, text="Bu tabloda kayıt bulunmamaktadır.")
        pdf.set_text_color(*PDF_COLOR_TEXT)
        return

    _draw_table_header(pdf, headers, col_widths, aligns)
    pdf.ln(1)

    line_h = 6.5
    pdf.set_font(pdf.font_regular, "", 9)

    for row_index, row in enumerate(rows):
        if pdf.get_y() + line_h > pdf.h - pdf.b_margin - 12:
            pdf.add_page()
            _draw_table_header(pdf, headers, col_widths, aligns)
            pdf.ln(1)
            pdf.set_font(pdf.font_regular, "", 9)

        is_muted = _is_muted_row(row)
        priority_color = None
        if row_colors and row_index < len(row_colors):
            priority_color = row_colors[row_index]

        row_y = pdf.get_y()

        for cell_index, (value, width, align) in enumerate(zip(row, col_widths, aligns)):
            text = str(value) if value is not None else ""

            cell_x = pdf.get_x()

            if use_priority_pill and cell_index == 0 and priority_color is not None:
                pill_h = line_h - 2
                pill_w = width - 4
                pill_y = row_y + 1
                pdf.set_fill_color(*priority_color)
                pdf.rect(cell_x, pill_y, pill_w, pill_h, "F")
                pdf.set_text_color(255, 255, 255)
                pdf.set_font(pdf.font_bold, "B", 8)
                pdf.set_xy(cell_x, pill_y)
                pdf.cell(pill_w, pill_h, text.upper(), align="C")
                pdf.set_xy(cell_x + width, row_y)
                pdf.set_text_color(*PDF_COLOR_TEXT)
                pdf.set_font(pdf.font_regular, "", 9)
                continue

            if is_muted:
                pdf.set_text_color(*PDF_COLOR_MUTED)
                pdf.set_font(pdf.font_regular, "", 9)
            elif priority_color is not None and cell_index == 0 and not use_priority_pill:
                pdf.set_text_color(*priority_color)
                pdf.set_font(pdf.font_bold, "B", 9)
            else:
                pdf.set_text_color(*PDF_COLOR_TEXT)
                pdf.set_font(pdf.font_regular, "", 9)

            pdf.cell(width, line_h, text, border=0, align=align)

            pdf.set_text_color(*PDF_COLOR_TEXT)
            pdf.set_font(pdf.font_regular, "", 9)

        pdf.ln(line_h)

        if row_index < len(rows) - 1:
            pdf.set_draw_color(*PDF_COLOR_DIVIDER)
            pdf.set_line_width(0.1)
            y_divider = pdf.get_y()
            pdf.line(pdf.l_margin, y_divider, pdf.l_margin + sum(col_widths), y_divider)


def _truncate(value, max_chars: int) -> str:
    text = str(value or "")
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1].rstrip() + "…"


def _draw_risk_table(pdf: ReportPDF, risks: dict) -> None:
    customers = risks.get("customers", []) or []

    def _sort_key(customer):
        try:
            score = int(customer.get("Risk Skoru", 0) or 0)
        except (TypeError, ValueError):
            score = 0
        return -score

    sorted_customers = sorted(customers, key=_sort_key)

    headers = ["Öncelik", "Müşteri", "Skor", "Risk Tipi", "Aksiyon"]
    col_widths = [22, 36, 12, 52, 58]
    aligns = ["C", "L", "C", "L", "L"]

    rows = []
    row_colors = []
    for customer in sorted_customers:
        priority = customer.get("Öncelik", "-")
        rows.append([
            priority,
            _truncate(customer.get("Müşteri", "-"), 22),
            customer.get("Risk Skoru", "-"),
            _truncate(customer.get("Risk Tipi", "-"), 34),
            _truncate(customer.get("Önerilen Aksiyon", "-"), 38),
        ])
        row_colors.append(PDF_PRIORITY_COLORS.get(priority))

    _draw_table(
        pdf,
        headers,
        rows,
        col_widths,
        aligns=aligns,
        row_colors=row_colors,
        use_priority_pill=True,
    )


def _draw_data_quality_table(pdf: ReportPDF, data_quality: dict) -> None:
    issues = data_quality.get("issues", []) or []
    headers = ["Satır", "Müşteri", "Problem", "Mevcut Değer", "Aksiyon"]
    col_widths = [14, 38, 38, 36, 54]
    aligns = ["C", "L", "L", "L", "L"]

    rows = []
    for issue in issues:
        rows.append([
            issue.get("Satır", "-"),
            _truncate(issue.get("Müşteri", "-"), 22),
            _truncate(issue.get("Problem", "-"), 24),
            _truncate(issue.get("Mevcut Değer", "-"), 22),
            _truncate(issue.get("Önerilen Aksiyon", "-"), 34),
        ])

    _draw_table(pdf, headers, rows, col_widths, aligns=aligns)


def _draw_breakdown_table(pdf: ReportPDF, items: list, label_key: str, label_header: str) -> None:
    headers = [label_header, "Satış Tutarı"]
    col_widths = [pdf.epw * 0.60, pdf.epw * 0.40]
    aligns = ["L", "R"]
    rows = [
        [
            str(item.get(label_key, "-")),
            str(item.get("sales_amount_formatted", "-")),
        ]
        for item in items
    ]
    _draw_table(pdf, headers, rows, col_widths, aligns=aligns)


def _draw_recommendations(pdf: ReportPDF, recommendations: list) -> None:
    pdf.set_text_color(*PDF_COLOR_TEXT)
    badge_size = 7
    for index, recommendation in enumerate(recommendations, start=1):
        if pdf.get_y() + 12 > pdf.h - pdf.b_margin - 12:
            pdf.add_page()

        y0 = pdf.get_y()

        pdf.set_fill_color(*PDF_COLOR_ACCENT)
        pdf.rect(pdf.l_margin, y0 + 1.2, badge_size, badge_size, "F")
        pdf.set_xy(pdf.l_margin, y0 + 1.2)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font(pdf.font_bold, "B", 9)
        pdf.cell(badge_size, badge_size, str(index), align="C")

        pdf.set_xy(pdf.l_margin + badge_size + 4, y0)
        pdf.set_text_color(*PDF_COLOR_TEXT)
        pdf.set_font(pdf.font_regular, "", 10.5)
        pdf.multi_cell(w=pdf.epw - badge_size - 4, h=6, text=str(recommendation))

        pdf.ln(2)


def create_pdf_report(analysis_result, output_path):
    pdf = ReportPDF()
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    _setup_pdf_fonts(pdf)

    source_file = analysis_result.get("source_file", "-")
    summary = analysis_result.get("summary", {})
    data_quality = analysis_result.get("data_quality", {})
    risks = analysis_result.get("risks", {})
    breakdowns = analysis_result.get("sales_breakdowns", {})
    recommendations = analysis_result.get("recommendations", [])

    _draw_cover_page(pdf, source_file)

    pdf.add_page()
    _draw_section_title(pdf, "Genel Bakış", eyebrow="01 · Özet Metrikler")
    _draw_kpi_cards(pdf, summary, data_quality, risks)
    pdf.ln(2)
    _draw_highlights(pdf, summary)
    pdf.ln(4)
    _draw_section_title(pdf, "Yönetici Özeti", eyebrow="02 · Karar Notu")
    _draw_executive_paragraph(pdf, summary, data_quality, risks)

    pdf.add_page()
    _draw_section_title(pdf, "Riskli Müşteriler", eyebrow="03 · Önceliklendirme")
    _draw_risk_table(pdf, risks)

    pdf.add_page()
    _draw_section_title(pdf, "Veri Kalite Problemleri", eyebrow="04 · Doğrulama")
    _draw_data_quality_table(pdf, data_quality)

    pdf.add_page()
    _draw_section_title(pdf, "Bölge Bazlı Satış", eyebrow="05 · Performans Kırılımı")
    _draw_breakdown_table(pdf, breakdowns.get("by_region", []), "region", "Bölge")
    pdf.ln(8)
    _draw_section_title(pdf, "Ürün Bazlı Satış", eyebrow="06 · Performans Kırılımı")
    _draw_breakdown_table(pdf, breakdowns.get("by_product", []), "product", "Ürün")

    pdf.add_page()
    _draw_section_title(pdf, "Satış Temsilcisi Bazlı Satış", eyebrow="07 · Performans Kırılımı")
    _draw_breakdown_table(pdf, breakdowns.get("by_sales_rep", []), "sales_rep", "Satış Temsilcisi")
    pdf.ln(8)
    _draw_section_title(pdf, "Öncelikli Aksiyon Planı", eyebrow="08 · Sonraki Adımlar")
    _draw_recommendations(pdf, recommendations)

    pdf.output(str(output_path))


def add_issue(issues, row_number, customer, issue_type, value, recommendation):
    issues.append(
        {
            "Satır": row_number,
            "Müşteri": customer or "Müşteri adı eksik",
            "Problem": issue_type,
            "Mevcut Değer": display_value(value),
            "Önerilen Aksiyon": recommendation,
        }
    )


def add_risk(risks, customer, risk_type, recommendation):
    risks.append(
        {
            "Müşteri": customer or "Müşteri adı eksik",
            "Risk Tipi": risk_type,
            "Önerilen Aksiyon": recommendation,
        }
    )


def calculate_risk_score(risk_type_text: str) -> int:
    risk_weights = {
        "Anormal yüksek satış": 5,
        "Negatif satış tutarı": 5,
        "Durum/ödeme tutarsızlığı": 4,
        "Eksik satış tutarı": 4,
        "Hatalı tarih": 3,
        "Geciken ödeme": 2,
    }

    score = 0

    for risk_name, weight in risk_weights.items():
        if risk_name in risk_type_text:
            score += weight

    return score


def get_risk_priority(score: int) -> str:
    if score >= 5:
        return "Yüksek"
    if score >= 3:
        return "Orta"
    return "Düşük"


def combine_unique(series, separator=" + ", clean_sentence=False):
    values = []

    for value in series:
        text = safe_text(value)

        if clean_sentence:
            text = text.rstrip(".")
            text = text[0].lower() + text[1:] if text else text

        if text and text not in values:
            values.append(text)

    combined = separator.join(values)

    if clean_sentence and combined:
        combined = combined[0].upper() + combined[1:] + "."

    return combined


def run_sales_analysis():
    OUTPUT_DIR.mkdir(exist_ok=True)

    excel_path = find_excel_file()
    print(f"Okunan dosya: {excel_path}")

    df = pd.read_excel(excel_path)
    df.columns = [str(col).strip() for col in df.columns]

    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Eksik kolonlar var: {missing_columns}")

    df["Satış Tutarı Temiz"] = df["Satış Tutarı"].apply(clean_amount)
    df["Tarih Temiz"] = pd.to_datetime(df["Tarih"], errors="coerce")

    total_sales = df["Satış Tutarı Temiz"].sum(skipna=True)

    won_sales_df = df[df["Durum"].apply(safe_text).str.lower() == "kazanıldı"]
    won_sales_total = won_sales_df["Satış Tutarı Temiz"].sum(skipna=True)

    pending_sales_count = len(
        df[df["Durum"].apply(safe_text).str.lower() == "beklemede"]
    )

    lost_sales_count = len(
        df[df["Durum"].apply(safe_text).str.lower() == "kaybedildi"]
    )

    positive_amounts = df[df["Satış Tutarı Temiz"] > 0]["Satış Tutarı Temiz"]
    median_amount = positive_amounts.median()

    issues = []
    risks = []

    for index, row in df.iterrows():
        row_number = index + 2
        customer = safe_text(row["Müşteri"])
        status = safe_text(row["Durum"])
        payment_status = safe_text(row["Ödeme Durumu"])
        region = safe_text(row["Bölge"])
        sales_rep = safe_text(row["Satış Temsilcisi"])
        amount = row["Satış Tutarı Temiz"]
        raw_date = row["Tarih"]

        if pd.isna(amount):
            add_issue(
                issues,
                row_number,
                customer,
                "Eksik satış tutarı",
                row["Satış Tutarı"],
                "Satış tutarı tamamlanmalı.",
            )
            add_risk(
                risks,
                customer,
                "Eksik satış tutarı",
                "Tutar bilgisi tamamlanmadan rapor hesaplamasına güvenilmemeli.",
            )

        if region == "":
            add_issue(
                issues,
                row_number,
                customer,
                "Eksik bölge",
                row["Bölge"],
                "Bölge bilgisi tamamlanmalı.",
            )

        if sales_rep == "":
            add_issue(
                issues,
                row_number,
                customer,
                "Eksik satış temsilcisi",
                row["Satış Temsilcisi"],
                "Satış temsilcisi bilgisi tamamlanmalı.",
            )

        if pd.isna(row["Tarih Temiz"]):
            add_issue(
                issues,
                row_number,
                customer,
                "Hatalı tarih",
                raw_date,
                "Tarih formatı kontrol edilmeli.",
            )
            add_risk(
                risks,
                customer,
                "Hatalı tarih",
                "Tarih düzeltilmeden dönemsel analiz yapılmamalı.",
            )

        if pd.notna(amount) and amount < 0:
            add_issue(
                issues,
                row_number,
                customer,
                "Negatif satış tutarı",
                amount,
                "Bu kayıt iade mi yoksa veri hatası mı kontrol edilmeli.",
            )
            add_risk(
                risks,
                customer,
                "Negatif satış tutarı",
                "Finans/muhasebe ekibi bu kaydı doğrulamalı.",
            )

        if status.lower() not in ALLOWED_STATUSES:
            add_issue(
                issues,
                row_number,
                customer,
                "Standart dışı durum değeri",
                status,
                "Durum alanı Kazanıldı, Beklemede veya Kaybedildi değerlerinden biri olmalı.",
            )

        if status.lower() == "kaybedildi" and payment_status.lower() == "ödendi":
            add_issue(
                issues,
                row_number,
                customer,
                "Durum/ödeme tutarsızlığı",
                f"Durum={status}, Ödeme Durumu={payment_status}",
                "Satış kaydı ve ödeme durumu birlikte doğrulanmalı.",
            )
            add_risk(
                risks,
                customer,
                "Durum/ödeme tutarsızlığı",
                "Kayıt satış veya finans ekibi tarafından kontrol edilmeli.",
            )

        if payment_status.lower() == "gecikti":
            add_risk(
                risks,
                customer,
                "Geciken ödeme",
                "Tahsilat takip listesine alınmalı.",
            )

        if (
            pd.notna(amount)
            and pd.notna(median_amount)
            and median_amount > 0
            and amount > median_amount * 5
        ):
            add_issue(
                issues,
                row_number,
                customer,
                "Anormal yüksek satış",
                amount,
                "Bu satış gerçek mi yoksa veri girişi hatası mı kontrol edilmeli.",
            )
            add_risk(
                risks,
                customer,
                "Anormal yüksek satış",
                "Gerçek satışsa stratejik müşteri olarak takip edilmeli; hataysa düzeltilmeli.",
            )

    issues_df = pd.DataFrame(issues)
    raw_risks_df = pd.DataFrame(risks).drop_duplicates()

    if raw_risks_df.empty:
        risks_df = pd.DataFrame(
            columns=[
                "Müşteri",
                "Risk Tipi",
                "Önerilen Aksiyon",
                "Risk Skoru",
                "Öncelik",
            ]
        )
    else:
        risks_df = (
            raw_risks_df
            .groupby("Müşteri", as_index=False)
            .agg(
                {
                    "Risk Tipi": lambda values: combine_unique(values, " + "),
                    "Önerilen Aksiyon": lambda values: combine_unique(
                        values,
                        "; ",
                        clean_sentence=True,
                    ),
                }
            )
        )

        risks_df["Risk Skoru"] = risks_df["Risk Tipi"].apply(calculate_risk_score)
        risks_df["Öncelik"] = risks_df["Risk Skoru"].apply(get_risk_priority)

        risks_df = risks_df.sort_values(
            by=["Risk Skoru", "Müşteri"],
            ascending=[False, True],
        ).reset_index(drop=True)

    valid_sales_df = df.dropna(subset=["Satış Tutarı Temiz"])

    region_summary = (
        valid_sales_df.groupby("Bölge", dropna=False)["Satış Tutarı Temiz"]
        .sum()
        .sort_values(ascending=False)
    )

    product_summary = (
        valid_sales_df.groupby("Ürün", dropna=False)["Satış Tutarı Temiz"]
        .sum()
        .sort_values(ascending=False)
    )

    sales_rep_summary = (
        valid_sales_df.groupby("Satış Temsilcisi", dropna=False)["Satış Tutarı Temiz"]
        .sum()
        .sort_values(ascending=False)
    )

    top_region = region_summary.index[0] if not region_summary.empty else "Bulunamadı"
    top_product = product_summary.index[0] if not product_summary.empty else "Bulunamadı"
    top_sales_rep = (
        sales_rep_summary.index[0] if not sales_rep_summary.empty else "Bulunamadı"
    )

    recommendations = [
        "Eksik, negatif ve hatalı tarih içeren kayıtlar düzeltilmeden nihai rapor kullanılmamalı.",
        "Geciken ödemeler için tahsilat takip listesi oluşturulmalı.",
        "Anormal yüksek satışlar gerçek mi veri hatası mı kontrol edilmeli.",
        "Beklemede olan satışlar için satış temsilcileri hızlı takip yapmalı.",
        "Durum alanı Kazanıldı, Beklemede, Kaybedildi değerleriyle standartlaştırılmalı.",
    ]

    markdown_lines = []

    markdown_lines.append("# Mayıs 2026 Satış Yönetici Raporu")
    markdown_lines.append("")
    markdown_lines.append("## 1. Yönetici Özeti")
    markdown_lines.append("")
    markdown_lines.append(
        f"Ham veriye göre toplam satış tutarı **{format_tl(total_sales)}** görünmektedir."
    )
    markdown_lines.append(
        f"Kazanılan satışların toplamı **{format_tl(won_sales_total)}** olarak hesaplanmıştır."
    )
    markdown_lines.append(
        f"En yüksek satış hacmi görünen bölge **{top_region}**, en güçlü ürün ise **{top_product}** olarak görünmektedir."
    )
    markdown_lines.append(
        f"En yüksek satış hacmine sahip satış temsilcisi **{top_sales_rep}** olarak hesaplanmıştır."
    )
    markdown_lines.append(
        "Ancak veri içinde kalite problemleri bulunduğu için bu rapor karar öncesi kontrol edilmelidir."
    )
    markdown_lines.append("")

    markdown_lines.append("## 2. En Önemli 5 Bulgu")
    markdown_lines.append("")
    markdown_lines.append(f"1. Toplam satış: **{format_tl(total_sales)}**")
    markdown_lines.append(f"2. Kazanılan satış toplamı: **{format_tl(won_sales_total)}**")
    markdown_lines.append(f"3. Beklemede olan satış sayısı: **{pending_sales_count}**")
    markdown_lines.append(f"4. Kaybedilen satış sayısı: **{lost_sales_count}**")
    markdown_lines.append(f"5. Riskli müşteri kaydı sayısı: **{len(risks_df)}**")
    markdown_lines.append("")

    markdown_lines.append("## 3. Veri Kalitesi Özeti")
    markdown_lines.append("")
    markdown_lines.append(f"- Toplam veri kalite problemi: **{len(issues_df)}**")
    markdown_lines.append(
        f"- Geciken ödeme veya finansal risk kaydı: **{len(risks_df)}**"
    )
    markdown_lines.append("")

    markdown_lines.append("## 4. Detaylı Veri Hataları")
    markdown_lines.append("")

    if issues_df.empty:
        markdown_lines.append("Veri kalitesi problemi bulunamadı.")
    else:
        markdown_lines.append("| Satır | Müşteri | Problem | Mevcut Değer | Önerilen Aksiyon |")
        markdown_lines.append("|---:|---|---|---|---|")

        for _, issue in issues_df.iterrows():
            markdown_lines.append(
                f"| {issue['Satır']} | {issue['Müşteri']} | {issue['Problem']} | {issue['Mevcut Değer']} | {issue['Önerilen Aksiyon']} |"
            )

    markdown_lines.append("")

    markdown_lines.append("## 5. Riskli Müşteriler")
    markdown_lines.append("")

    if risks_df.empty:
        markdown_lines.append("Riskli müşteri bulunamadı.")
    else:
        markdown_lines.append("| Öncelik | Müşteri | Risk Tipi | Risk Skoru | Önerilen Aksiyon |")
        markdown_lines.append("|---|---|---|---:|---|")

        for _, risk in risks_df.iterrows():
            markdown_lines.append(
                f"| {risk['Öncelik']} | {risk['Müşteri']} | {risk['Risk Tipi']} | {risk['Risk Skoru']} | {risk['Önerilen Aksiyon']} |"
            )

    markdown_lines.append("")

    markdown_lines.append("## 6. Aksiyon Önerileri")
    markdown_lines.append("")

    for index, recommendation in enumerate(recommendations, start=1):
        markdown_lines.append(f"{index}. {recommendation}")

    markdown_lines.append("")

    markdown_lines.append("## 7. Bölge Bazlı Satış Özeti")
    markdown_lines.append("")
    markdown_lines.append("| Bölge | Satış Tutarı |")
    markdown_lines.append("|---|---:|")
    for region, value in region_summary.items():
        region_name = region if safe_text(region) else "Bölge eksik"
        markdown_lines.append(f"| {region_name} | {format_tl(value)} |")

    markdown_lines.append("")

    markdown_lines.append("## 8. Ürün Bazlı Satış Özeti")
    markdown_lines.append("")
    markdown_lines.append("| Ürün | Satış Tutarı |")
    markdown_lines.append("|---|---:|")
    for product, value in product_summary.items():
        product_name = product if safe_text(product) else "Ürün eksik"
        markdown_lines.append(f"| {product_name} | {format_tl(value)} |")

    markdown_lines.append("")

    markdown_lines.append("## 9. Satış Temsilcisi Bazlı Satış Özeti")
    markdown_lines.append("")
    markdown_lines.append("| Satış Temsilcisi | Satış Tutarı |")
    markdown_lines.append("|---|---:|")
    for rep, value in sales_rep_summary.items():
        rep_name = rep if safe_text(rep) else "Satış temsilcisi eksik"
        markdown_lines.append(f"| {rep_name} | {format_tl(value)} |")

    report_path = OUTPUT_DIR / "generated_report_v4.md"
    pdf_path = OUTPUT_DIR / "generated_report_v4.pdf"
    json_path = OUTPUT_DIR / "analysis_result_v4.json"
    issues_path = OUTPUT_DIR / "data_quality_issues.csv"
    risks_path = OUTPUT_DIR / "risky_customers.csv"

    analysis_result = {
        "version": "v10.3",
        "source_file": excel_path.name,
        "summary": {
            "total_sales": float(total_sales),
            "total_sales_formatted": format_tl(total_sales),
            "won_sales_total": float(won_sales_total),
            "won_sales_total_formatted": format_tl(won_sales_total),
            "pending_sales_count": int(pending_sales_count),
            "lost_sales_count": int(lost_sales_count),
            "top_region": safe_text(top_region),
            "top_product": safe_text(top_product),
            "top_sales_rep": safe_text(top_sales_rep),
        },
        "data_quality": {
            "issue_count": int(len(issues_df)),
            "issues": dataframe_to_records(issues_df),
        },
        "risks": {
            "risk_customer_count": int(len(risks_df)),
            "customers": dataframe_to_records(risks_df),
        },
        "sales_breakdowns": {
            "by_region": series_to_records(
                region_summary,
                "region",
                "sales_amount",
                "Bölge eksik",
            ),
            "by_product": series_to_records(
                product_summary,
                "product",
                "sales_amount",
                "Ürün eksik",
            ),
            "by_sales_rep": series_to_records(
                sales_rep_summary,
                "sales_rep",
                "sales_amount",
                "Satış temsilcisi eksik",
            ),
        },
        "recommendations": recommendations,
    }

    with open(report_path, "w", encoding="utf-8") as file:
        file.write("\n".join(markdown_lines))

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(analysis_result, file, ensure_ascii=False, indent=2)

    issues_df.to_csv(issues_path, index=False, encoding="utf-8-sig")
    risks_df.to_csv(risks_path, index=False, encoding="utf-8-sig")

    create_pdf_report(analysis_result, pdf_path)

    print("")
    print("Analiz tamamlandı.")
    print(f"Markdown rapor oluşturuldu: {report_path}")
    print(f"Veri kalite sorunları oluşturuldu: {issues_path}")
    print(f"Riskli müşteriler oluşturuldu: {risks_path}")
    print(f"PDF rapor oluşturuldu: {pdf_path}")
    print(f"JSON analiz sonucu oluşturuldu: {json_path}")

    return analysis_result


def main():
    return run_sales_analysis()


if __name__ == "__main__":
    main()