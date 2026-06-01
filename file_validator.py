import hashlib
import json
from pathlib import Path
from io import BytesIO

import pandas as pd

from report_schemas.sales import (
    COLUMN_ALIASES,
    OPTIONAL_AUTO_FILL_VALUES,
    REQUIRED_COLUMNS,
    TEMPLATE_SAMPLE_DATA,
)


NO_MAPPING_LABEL = "Eşleştirme yok / otomatik doldur"

COLUMN_MAPPINGS_FILE = Path(__file__).resolve().parent / ".column_mappings.json"


def create_template_excel_bytes():
    df = pd.DataFrame(TEMPLATE_SAMPLE_DATA)
    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Sales Demo Data")

    return output.getvalue()


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [str(col).strip() for col in df.columns]
    return df


def find_missing_columns(df: pd.DataFrame):
    df = normalize_columns(df)
    return [column for column in REQUIRED_COLUMNS if column not in df.columns]


def validate_uploaded_excel(uploaded_file):
    file_bytes = uploaded_file.getvalue()

    try:
        preview_df = pd.read_excel(BytesIO(file_bytes))
        preview_df = normalize_columns(preview_df)
    except Exception as error:
        return False, None, [f"Excel dosyası okunamadı: {error}"], file_bytes

    missing_columns = find_missing_columns(preview_df)

    if missing_columns:
        return False, preview_df, missing_columns, file_bytes

    return True, preview_df, [], file_bytes


def validate_existing_excel_file(file_path: Path):
    if not file_path.exists():
        return False, ["Excel dosyası bulunamadı."]

    try:
        df = pd.read_excel(file_path)
        df = normalize_columns(df)
    except Exception as error:
        return False, [f"Excel dosyası okunamadı: {error}"]

    missing_columns = find_missing_columns(df)

    if missing_columns:
        return False, missing_columns

    return True, []


def normalize_column_name(value: str) -> str:
    return str(value or "").strip().casefold()


def get_column_signature(columns) -> str:
    normalized = sorted(normalize_column_name(column) for column in columns)
    joined = "|".join(normalized)
    return hashlib.sha256(joined.encode("utf-8")).hexdigest()[:16]


def load_saved_mappings() -> dict:
    if not COLUMN_MAPPINGS_FILE.exists():
        return {}

    try:
        with open(COLUMN_MAPPINGS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def get_saved_mapping_for_columns(columns):
    mappings = load_saved_mappings()
    signature = get_column_signature(columns)
    return mappings.get(signature)


def has_saved_mapping_for_columns(columns) -> bool:
    return get_saved_mapping_for_columns(columns) is not None


def save_mapping_for_columns(columns, column_mapping: dict) -> None:
    mappings = load_saved_mappings()
    signature = get_column_signature(columns)
    mappings[signature] = column_mapping

    with open(COLUMN_MAPPINGS_FILE, "w", encoding="utf-8") as file:
        json.dump(mappings, file, ensure_ascii=False, indent=2)


def guess_column_match(required_column: str, uploaded_columns):
    aliases = COLUMN_ALIASES.get(required_column, [required_column])

    normalized_uploaded_columns = {
        normalize_column_name(column): column for column in uploaded_columns
    }

    for alias in aliases:
        normalized_alias = normalize_column_name(alias)

        if normalized_alias in normalized_uploaded_columns:
            return normalized_uploaded_columns[normalized_alias]

    return None


def get_column_mapping_defaults(df: pd.DataFrame) -> dict:
    df = normalize_columns(df)
    uploaded_columns = list(df.columns)
    valid_saved_values = set(uploaded_columns) | {NO_MAPPING_LABEL}

    saved_mapping = get_saved_mapping_for_columns(uploaded_columns)

    mapping_defaults = {}

    for required_column in REQUIRED_COLUMNS:
        if saved_mapping is not None:
            saved_value = saved_mapping.get(required_column)
            if saved_value in valid_saved_values:
                mapping_defaults[required_column] = saved_value
                continue

        mapping_defaults[required_column] = guess_column_match(
            required_column,
            uploaded_columns,
        )

    return mapping_defaults


def build_mapped_dataframe(df: pd.DataFrame, column_mapping: dict) -> pd.DataFrame:
    df = normalize_columns(df)

    mapped_df = pd.DataFrame()
    missing_required_columns = []
    used_uploaded_columns = []

    for required_column in REQUIRED_COLUMNS:
        selected_column = column_mapping.get(required_column)

        if selected_column == NO_MAPPING_LABEL:
            selected_column = None

        if selected_column and selected_column in df.columns:
            if selected_column in used_uploaded_columns:
                raise ValueError(
                    f"'{selected_column}' kolonu birden fazla sistem alanına eşleştirildi. "
                    "Lütfen her Excel kolonunu yalnızca bir kez kullan."
                )

            mapped_df[required_column] = df[selected_column]
            used_uploaded_columns.append(selected_column)

        elif required_column in OPTIONAL_AUTO_FILL_VALUES:
            mapped_df[required_column] = OPTIONAL_AUTO_FILL_VALUES[required_column]

        else:
            missing_required_columns.append(required_column)

    if missing_required_columns:
        raise ValueError(
            "Zorunlu alanlar eşleştirilmedi: "
            + ", ".join(missing_required_columns)
        )

    return mapped_df[REQUIRED_COLUMNS]


def create_excel_bytes_from_dataframe(df: pd.DataFrame):
    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Sales Demo Data")

    return output.getvalue()