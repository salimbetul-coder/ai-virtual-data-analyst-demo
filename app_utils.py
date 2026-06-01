from pathlib import Path
from io import StringIO
import contextlib
import json

import pandas as pd
import streamlit as st


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def read_bytes(path: Path):
    if not path.exists():
        return None
    return path.read_bytes()


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def read_csv_safely(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()

    try:
        return pd.read_csv(path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()


def clean_ai_summary_text(text: str) -> str:
    text = text.strip()

    if text.startswith("# AI Yönetici Yorumu"):
        text = text.replace("# AI Yönetici Yorumu", "", 1).strip()

    return text


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


def run_function_with_logs(function):
    log_output = StringIO()

    try:
        with contextlib.redirect_stdout(log_output), contextlib.redirect_stderr(log_output):
            result = function()

        return True, log_output.getvalue(), result

    except Exception as error:
        error_output = log_output.getvalue()
        error_output += f"\nHata oluştu: {error}"

        return False, error_output, None


def show_download_button(label: str, path: Path, mime: str, download_name: str = None):
    file_bytes = read_bytes(path)

    if file_bytes is None:
        st.warning(f"{path.name} henüz oluşmadı.")
        return

    st.download_button(
        label=label,
        data=file_bytes,
        file_name=download_name or path.name,
        mime=mime,
        use_container_width=True,
    )