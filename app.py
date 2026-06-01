from pathlib import Path

import pandas as pd
import streamlit as st

from analyze_sales import run_sales_analysis
from generate_ai_summary import generate_ai_summary
from file_validator import (
    NO_MAPPING_LABEL,
    REQUIRED_COLUMNS,
    build_mapped_dataframe,
    create_excel_bytes_from_dataframe,
    create_template_excel_bytes,
    get_column_mapping_defaults,
    has_saved_mapping_for_columns,
    save_mapping_for_columns,
    validate_existing_excel_file,
    validate_uploaded_excel,
)
from app_utils import (
    read_text,
    read_json,
    read_csv_safely,
    clean_ai_summary_text,
    run_function_with_logs,
    show_download_button,
)


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

EXCEL_PATH = DATA_DIR / "Sales Demo Data.xlsx"

AI_SUMMARY_PATH = OUTPUT_DIR / "generated_ai_summary_v5.md"
REPORT_V5_PATH = OUTPUT_DIR / "generated_report_v5.md"
REPORT_V4_PATH = OUTPUT_DIR / "generated_report_v4.md"
PDF_V4_PATH = OUTPUT_DIR / "generated_report_v4.pdf"
JSON_PATH = OUTPUT_DIR / "analysis_result_v4.json"
ISSUES_CSV_PATH = OUTPUT_DIR / "data_quality_issues.csv"
RISKS_CSV_PATH = OUTPUT_DIR / "risky_customers.csv"


st.set_page_config(
    page_title="AI Virtual Data Analyst",
    page_icon="📊",
    layout="wide",
)


st.markdown(
    """
    <style>
    .block-container {
        padding-top: 4rem;
        max-width: 1200px;
    }

    h1 {
        font-size: 34px !important;
        margin-top: 20px !important;
    }

    h2 {
        font-size: 26px !important;
        margin-top: 28px !important;
    }

    h3 {
        font-size: 20px !important;
    }

    p, li {
        font-size: 16px !important;
        line-height: 1.7 !important;
    }

    .main-title {
        font-size: 46px;
        font-weight: 800;
        margin-bottom: 4px;
    }

    .subtitle {
        font-size: 18px;
        color: #9ca3af;
        margin-bottom: 24px;
    }

    .kpi-card {
        padding: 22px;
        border-radius: 18px;
        background: #111827;
        border: 1px solid #374151;
        min-height: 125px;
    }

    .kpi-label {
        font-size: 14px;
        color: #9ca3af;
        margin-bottom: 8px;
    }

    .kpi-value {
        font-size: 28px;
        font-weight: 800;
        color: #f9fafb;
    }

    .kpi-note {
        font-size: 13px;
        color: #9ca3af;
        margin-top: 8px;
    }

    .section-card {
        padding: 18px;
        border-radius: 16px;
        background: #0f172a;
        border: 1px solid #334155;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def render_kpi_card(label: str, value: str, note: str = ""):
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_status_box():
    if REPORT_V5_PATH.exists() and JSON_PATH.exists():
        st.success("Şu anda örnek veri ile hazırlanmış demo raporu görüyorsun. Kendi Excel'ini yükleyip yeniden analiz edebilirsin.")
    else:
        st.info("Henüz rapor oluşmadı. Excel dosyası yükleyip Analiz Et butonuna bas.")


def create_risk_action_summary(risk_type: str) -> str:
    risk_type = str(risk_type or "")

    has_outlier = "Anormal yüksek satış" in risk_type
    has_negative = "Negatif satış tutarı" in risk_type
    has_inconsistency = "Durum/ödeme tutarsızlığı" in risk_type
    has_missing_amount = "Eksik satış tutarı" in risk_type
    has_invalid_date = "Hatalı tarih" in risk_type
    has_late_payment = "Geciken ödeme" in risk_type

    if has_outlier and has_inconsistency:
        return "Satış, ödeme ve yüksek tutar kaydı doğrulansın."

    if has_outlier:
        return "Yüksek tutarlı satış doğrulansın."

    if has_negative and has_late_payment:
        return "Negatif tutar ve tahsilat durumu kontrol edilsin."

    if has_negative:
        return "Negatif tutar finans ekibiyle kontrol edilsin."

    if has_missing_amount and has_late_payment:
        return "Eksik tutar tamamlanıp tahsilat takibi yapılsın."

    if has_missing_amount:
        return "Eksik satış tutarı tamamlanmalı."

    if has_invalid_date and has_late_payment:
        return "Tarih ve tahsilat kaydı kontrol edilsin."

    if has_invalid_date:
        return "Tarih bilgisi düzeltilmeli."

    if has_inconsistency:
        return "Satış ve ödeme durumu birlikte doğrulansın."

    if has_late_payment:
        return "Tahsilat takip listesine alınsın."

    return "Detaylı aksiyon metni kontrol edilsin."


def prepare_risk_display_df(risks_df: pd.DataFrame, priority_filter: str = "Tümü"):
    if risks_df.empty:
        return pd.DataFrame(), pd.DataFrame()

    filtered_df = risks_df.copy()

    if priority_filter != "Tümü" and "Öncelik" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["Öncelik"] == priority_filter]

    if filtered_df.empty:
        return pd.DataFrame(), filtered_df

    if "Risk Tipi" in filtered_df.columns:
        filtered_df["Aksiyon Özeti"] = filtered_df["Risk Tipi"].apply(
            create_risk_action_summary
        )
    else:
        filtered_df["Aksiyon Özeti"] = "Detaylı aksiyon metni kontrol edilsin."

    display_columns = [
        "Öncelik",
        "Müşteri",
        "Risk Skoru",
        "Risk Tipi",
        "Aksiyon Özeti",
    ]

    existing_display_columns = [
        column for column in display_columns if column in filtered_df.columns
    ]

    return filtered_df[existing_display_columns], filtered_df


st.markdown('<div class="main-title">AI Virtual Data Analyst</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Excel’den 5 dakikada yönetici raporu, veri kalite kontrolü ve aksiyon önerileri.</div>',
    unsafe_allow_html=True,
)

render_status_box()

st.divider()

analysis_data = read_json(JSON_PATH)
summary = analysis_data.get("summary", {})
data_quality = analysis_data.get("data_quality", {})
risks = analysis_data.get("risks", {})

if analysis_data:
    st.subheader("Genel Durum")

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        render_kpi_card(
            "Toplam Satış",
            summary.get("total_sales_formatted", "-"),
            "Ham satış verisine göre hesaplandı",
        )

    with kpi2:
        render_kpi_card(
            "Kazanılan Satış",
            summary.get("won_sales_total_formatted", "-"),
            "Kazanıldı durumundaki kayıtlar",
        )

    with kpi3:
        render_kpi_card(
            "Veri Kalite Problemi",
            str(data_quality.get("issue_count", "-")),
            "Eksik, hatalı veya tutarsız kayıtlar",
        )

    with kpi4:
        render_kpi_card(
            "Riskli Müşteri",
            str(risks.get("risk_customer_count", "-")),
            "Takip edilmesi gereken müşteri kayıtları",
        )

    st.markdown("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info(f"En güçlü bölge: **{summary.get('top_region', '-')}**")

    with c2:
        st.info(f"En güçlü ürün: **{summary.get('top_product', '-')}**")

    with c3:
        st.info(f"En güçlü temsilci: **{summary.get('top_sales_rep', '-')}**")

st.divider()

left_col, right_col = st.columns([1.15, 1])


with left_col:
    st.subheader("1. Excel Dosyası Yükle")

    template_bytes = create_template_excel_bytes()

    st.download_button(
        label="Örnek Excel Şablonunu İndir",
        data=template_bytes,
        file_name="sales_report_template.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True,
    )

    uploaded_file = st.file_uploader(
        "Satış Excel dosyanı yükle",
        type=["xlsx"],
    )

    if uploaded_file is not None:
        is_valid, preview_df, validation_messages, file_bytes = validate_uploaded_excel(uploaded_file)

        if is_valid:
            DATA_DIR.mkdir(exist_ok=True)

            with open(EXCEL_PATH, "wb") as file:
                file.write(file_bytes)

            st.success("Dosya doğrulandı ve analiz için kaydedildi.")

            with st.expander("Yüklenen dosya önizlemesi"):
                st.dataframe(preview_df.head(5), use_container_width=True)

        else:
            st.warning("Yüklenen Excel dosyası beklenen kolon yapısıyla birebir eşleşmiyor.")

            if preview_df is None:
                st.error("Excel dosyası okunamadı.")
                st.write(validation_messages)

            else:
                st.info(
                    "Kolon eşleştirme ekranı aktif. "
                    "Aşağıda sistem alanlarını Excel dosyandaki kolonlarla eşleştirebilirsin."
                )

                with st.expander("Yüklenen dosyanın kolonları"):
                    st.write(list(preview_df.columns))

                if validation_messages:
                    with st.expander("Eksik görünen sistem kolonları"):
                        st.write(validation_messages)

                mapping_defaults = get_column_mapping_defaults(preview_df)
                uploaded_columns = [NO_MAPPING_LABEL] + list(preview_df.columns)

                if has_saved_mapping_for_columns(list(preview_df.columns)):
                    st.success(
                        "Bu dosya yapısı için daha önce kaydedilmiş eşleştirme bulundu. "
                        "Otomatik olarak yüklendi; istersen aşağıdan değiştirebilirsin."
                    )

                st.markdown("### Kolon Eşleştirme")

                column_mapping = {}

                map_col_1, map_col_2 = st.columns(2)

                for index, required_column in enumerate(REQUIRED_COLUMNS):
                    default_column = mapping_defaults.get(required_column)

                    if default_column in uploaded_columns:
                        default_index = uploaded_columns.index(default_column)
                    else:
                        default_index = 0

                    target_container = map_col_1 if index % 2 == 0 else map_col_2

                    with target_container:
                        selected_column = st.selectbox(
                            label=f"{required_column}",
                            options=uploaded_columns,
                            index=default_index,
                            key=f"mapping_{required_column}",
                        )

                    column_mapping[required_column] = selected_column

                if st.button(
                    "Kolonları Eşleştir ve Kaydet",
                    type="primary",
                    use_container_width=True,
                ):
                    try:
                        mapped_df = build_mapped_dataframe(
                            preview_df,
                            column_mapping,
                        )

                        mapped_excel_bytes = create_excel_bytes_from_dataframe(mapped_df)

                        DATA_DIR.mkdir(exist_ok=True)

                        with open(EXCEL_PATH, "wb") as file:
                            file.write(mapped_excel_bytes)

                        save_mapping_for_columns(
                            list(preview_df.columns),
                            column_mapping,
                        )

                        st.success(
                            "Kolonlar başarıyla eşleştirildi ve analiz formatına dönüştürüldü. "
                            "Eşleştirme kaydedildi; aynı yapıdaki dosyalarda otomatik kullanılacak."
                        )

                        with st.expander("Eşleştirilmiş dosya önizlemesi", expanded=True):
                            st.dataframe(mapped_df.head(5), use_container_width=True)

                    except ValueError as error:
                        st.error(str(error))

    else:
        if EXCEL_PATH.exists():
            st.info("Yeni dosya yüklenmedi. Mevcut demo Excel dosyası kullanılacak.")
        else:
            st.warning("Henüz Excel dosyası yok. Lütfen bir .xlsx dosyası yükle.")


with right_col:
    st.subheader("2. Analizi Çalıştır")

    st.markdown(
        """
        Analiz Et butonuna basınca:

        1. Excel verisini analiz eder.  
        2. Veri kalite sorunlarını çıkarır.  
        3. Riskli müşterileri belirler.  
        4. Yönetici yorum raporunu oluşturur.  
        """
    )

    analyze_button = st.button("Analiz Et", type="primary", use_container_width=True)

    if analyze_button:
        if not EXCEL_PATH.exists():
            st.error("Analiz için önce Excel dosyası yüklemelisin.")
        else:
            is_valid_file, validation_messages = validate_existing_excel_file(EXCEL_PATH)

            if not is_valid_file:
                st.error("Mevcut Excel dosyası analiz için uygun değil.")
                st.write(validation_messages)
                st.stop()

            with st.spinner("Python analiz motoru çalışıyor..."):
                success, output, analysis_result = run_function_with_logs(run_sales_analysis)

            with st.expander("İşlem detayı (analiz motoru)"):
                st.code(output)

            if not success:
                st.error("Analiz sırasında hata oluştu.")
                st.stop()

            with st.spinner("AI yönetici yorumu oluşturuluyor..."):
                success, output, ai_summary_result = run_function_with_logs(generate_ai_summary)

            with st.expander("İşlem detayı (AI yorum)"):
                st.code(output)

            if not success:
                st.error("AI yorum katmanı çalışırken hata oluştu.")
                st.stop()

            st.success("Analiz tamamlandı. Raporlar oluşturuldu.")
            st.rerun()


st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "AI Yönetici Yorumu",
        "Teknik Rapor",
        "Veri Kalitesi",
        "Riskli Müşteriler",
        "İndir",
    ]
)

with tab1:
    st.subheader("AI Yönetici Yorumu")

    ai_summary = read_text(AI_SUMMARY_PATH)

    if ai_summary:
        st.markdown(clean_ai_summary_text(ai_summary))
    else:
        st.info("Henüz AI yönetici yorumu oluşmadı. Önce Analiz Et butonuna bas.")


with tab2:
    st.subheader("Teknik Analiz Raporu")

    report = read_text(REPORT_V4_PATH)

    if report:
        st.markdown(report)
    else:
        st.info("Henüz teknik rapor oluşmadı.")


with tab3:
    st.subheader("Veri Kalitesi Sorunları")

    issues_df = read_csv_safely(ISSUES_CSV_PATH)

    if not ISSUES_CSV_PATH.exists():
        st.info("Henüz veri kalitesi CSV çıktısı oluşmadı.")
    elif issues_df.empty:
        st.success("Veri kalite sorunu bulunamadı.")
    else:
        st.dataframe(issues_df, use_container_width=True)


with tab4:
    st.subheader("Riskli Müşteriler")

    risks_df = read_csv_safely(RISKS_CSV_PATH)

    if not RISKS_CSV_PATH.exists():
        st.info("Henüz riskli müşteriler CSV çıktısı oluşmadı.")

    elif risks_df.empty:
        st.success("Riskli müşteri bulunamadı.")

    else:
        st.caption(
            "Riskli müşteriler öncelik ve risk skoruna göre listelenir. "
            "Uzun aksiyon metinleri ana tabloda kısaltılmıştır."
        )

        priority_options = ["Tümü"]

        if "Öncelik" in risks_df.columns:
            existing_priorities = risks_df["Öncelik"].dropna().unique().tolist()

            for priority in ["Yüksek", "Orta", "Düşük"]:
                if priority in existing_priorities:
                    priority_options.append(priority)

        priority_filter = st.selectbox(
            "Öncelik filtresi",
            priority_options,
            index=0,
        )

        display_df, detail_df = prepare_risk_display_df(
            risks_df,
            priority_filter=priority_filter,
        )

        if "Öncelik" in risks_df.columns:
            high_risk_count = int((risks_df["Öncelik"] == "Yüksek").sum())

            if high_risk_count > 0:
                st.warning(
                    f"Bu raporda {high_risk_count} yüksek öncelikli riskli müşteri bulunuyor."
                )

        if display_df.empty:
            st.info("Seçilen öncelik seviyesinde riskli müşteri bulunamadı.")

        else:
            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True,
            )

            with st.expander("Detaylı aksiyon metinlerini göster"):
                detail_columns = [
                    "Öncelik",
                    "Müşteri",
                    "Risk Skoru",
                    "Risk Tipi",
                    "Önerilen Aksiyon",
                ]

                existing_detail_columns = [
                    column for column in detail_columns if column in detail_df.columns
                ]

                st.dataframe(
                    detail_df[existing_detail_columns],
                    use_container_width=True,
                    hide_index=True,
                )


with tab5:
    st.subheader("Raporları İndir")
    st.caption("Analiz çıktıları yönetici raporu, teknik analiz ve veri kontrol dosyaları olarak indirilebilir.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Yönetici Raporları")

        show_download_button(
            "AI Yönetici Yorumu",
            AI_SUMMARY_PATH,
            "text/markdown",
            "ai_yonetici_yorumu.md",
        )

        show_download_button(
            "Birleşik Yönetici Raporu",
            REPORT_V5_PATH,
            "text/markdown",
            "yonetici_raporu.md",
        )

    with col2:
        st.markdown("### Sunum / Paylaşım")

        show_download_button(
            "PDF Yönetici Raporu",
            PDF_V4_PATH,
            "application/pdf",
            "yonetici_raporu.pdf",
        )

        show_download_button(
            "Teknik JSON Analiz Sonucu",
            JSON_PATH,
            "application/json",
            "analiz_sonucu.json",
        )

    with col3:
        st.markdown("### Kontrol Dosyaları")

        show_download_button(
            "Veri Kalite Sorunları",
            ISSUES_CSV_PATH,
            "text/csv",
            "veri_kalite_sorunlari.csv",
        )

        show_download_button(
            "Riskli Müşteriler",
            RISKS_CSV_PATH,
            "text/csv",
            "riskli_musteriler.csv",
        )


st.divider()

with st.expander("Bu demo ne yapıyor?"):
    st.markdown(
        """
Bu demo, BI ekibi olmayan küçük/orta ölçekli şirketler için tasarlanmış AI destekli sanal veri analisti uygulamasıdır.

Akış:

1. Kullanıcı Excel dosyası yükler.
2. Python analiz motoru satış verisini okur.
3. Toplam satış, kazanılan satış, bölge/ürün/temsilci kırılımları hesaplanır.
4. Eksik, hatalı ve tutarsız veriler tespit edilir.
5. Riskli müşteriler çıkarılır.
6. Yöneticiye uygun AI yorum raporu oluşturulur.
7. Markdown, PDF, CSV ve JSON çıktıları indirilebilir.
"""
    )