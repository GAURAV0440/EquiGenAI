import os
import json

from google import genai
from dotenv import load_dotenv

from src.prompts import REPORT_EXTRACTION_PROMPT

load_dotenv()


class FinancialAnalyzer:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model_name = os.getenv(
            "MODEL_NAME",
            "gemini-2.5-flash"
        )

    def analyze(self, document_text: str):

        document_text = document_text[:30000]

        prompt = f"""
{REPORT_EXTRACTION_PROMPT}

DOCUMENT:

{document_text}
"""

        try:

            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )

            raw_response = (
                response.text.strip()
                if response.text
                else ""
            )

            cleaned_response = (
                raw_response
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

            analysis = json.loads(
                cleaned_response
            )

            required_fields = [
                "company_name",
                "sector",
                "company_description",
                "investment_thesis",
                "key_highlights",
                "financial_metrics",
                "growth_drivers",
                "risks",
                "outlook",
                "recommendation"
            ]

            for field in required_fields:

                if field not in analysis:

                    analysis[field] = (
                        [] if field in [
                            "investment_thesis",
                            "key_highlights",
                            "growth_drivers",
                            "risks"
                        ]
                        else {}
                        if field == "financial_metrics"
                        else ""
                    )

            financial_metrics = analysis.get(
                "financial_metrics",
                {}
            )

            metric_fields = [
                "revenue",
                "revenue_growth",
                "ebitda",
                "ebitda_margin",
                "pat",
                "pat_growth"
            ]

            for field in metric_fields:

                if field not in financial_metrics:

                    financial_metrics[field] = ""

            analysis["financial_metrics"] = (
                financial_metrics
            )

            return analysis
        

        except json.JSONDecodeError:

            print(
                "\n========== RAW GEMINI RESPONSE ==========\n"
            )

            print(raw_response)

            raise Exception(
                "Gemini returned invalid JSON."
            )

        except Exception as e:

            raise Exception(
                f"Analysis Error: {str(e)}"
            )