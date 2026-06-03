import fitz
import pandas as pd
from pathlib import Path


class DocumentExtractor:
    """Extract text from PDF, TXT and CSV files."""

    @staticmethod
    def extract_pdf(file_path: str) -> str:
        text_parts = []

        try:
            with fitz.open(file_path) as doc:
                for page in doc:
                    page_text = page.get_text("text")
                    if page_text:
                        text_parts.append(page_text)

            return "\n".join(text_parts).strip()

        except Exception as e:
            raise Exception(f"Error extracting PDF: {str(e)}")

    @staticmethod
    def extract_txt(file_path: str) -> str:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read().strip()

        except Exception as e:
            raise Exception(f"Error extracting TXT: {str(e)}")

    @staticmethod
    def extract_csv(file_path: str) -> str:
        try:
            df = pd.read_csv(file_path)

            return (
                f"CSV Columns:\n{', '.join(df.columns)}\n\n"
                f"CSV Data:\n{df.to_string(index=False)}"
            )

        except Exception as e:
            raise Exception(f"Error extracting CSV: {str(e)}")

    @classmethod
    def extract(cls, file_path: str) -> str:
        file_path = str(file_path)

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return cls.extract_pdf(file_path)

        elif extension == ".txt":
            return cls.extract_txt(file_path)

        elif extension == ".csv":
            return cls.extract_csv(file_path)

        raise ValueError(
            f"Unsupported file type: {extension}. "
            "Supported formats: PDF, TXT, CSV"
        )