from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

PROMPT_INPUT = OUTPUT_DIR / "ai_prompt_v5.txt"
TECHNICAL_REPORT_INPUT = OUTPUT_DIR / "generated_report_v4.md"

AI_SUMMARY_OUTPUT = OUTPUT_DIR / "generated_ai_summary_api_v5.md"
FINAL_REPORT_OUTPUT = OUTPUT_DIR / "generated_report_api_v5.md"


def load_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Dosya bulunamadı: {path}")

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def save_text(path: Path, content: str) -> None:
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def main():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    model_name = os.getenv("OPENAI_MODEL", "gpt-5.5")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY bulunamadı. .env dosyasına OPENAI_API_KEY eklemelisin."
        )

    client = OpenAI(api_key=api_key)

    prompt = load_text(PROMPT_INPUT)
    technical_report = load_text(TECHNICAL_REPORT_INPUT)

    print("")
    print("OpenAI API isteği gönderiliyor...")
    print(f"Kullanılan model: {model_name}")

    response = client.responses.create(
        model=model_name,
        input=prompt,
    )

    ai_summary = response.output_text

    save_text(AI_SUMMARY_OUTPUT, ai_summary)

    final_report = f"""{ai_summary}

---

# Teknik Analiz Raporu

{technical_report}
"""

    save_text(FINAL_REPORT_OUTPUT, final_report)

    print("")
    print("v5.1 gerçek AI yorum katmanı oluşturuldu.")
    print(f"AI yorum dosyası: {AI_SUMMARY_OUTPUT}")
    print(f"Birleşik API rapor dosyası: {FINAL_REPORT_OUTPUT}")


if __name__ == "__main__":
    main()