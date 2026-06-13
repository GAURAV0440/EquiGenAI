REPORT_EXTRACTION_PROMPT = """
You are a senior equity research analyst.

Analyze the provided financial document.

Extract only information explicitly available in the document.

Return ONLY valid JSON.

{
    "company_name": "",
    "sector": "",

    "company_description": "",

    "investment_thesis": [
        "",
        "",
        ""
    ],

    "key_highlights": [
        "",
        "",
        "",
        ""
    ],

    "financial_metrics": {
        "revenue": "",
        "revenue_growth": "",
        "ebitda": "",
        "ebitda_margin": "",
        "pat": "",
        "pat_growth": "",
        "source_metric_revenue": "",
        "source_metric_ebitda": "",
        "source_metric_pat": ""
    },

    "growth_drivers": [
        "",
        "",
        ""
    ],

    "risks": [
        "",
        "",
        ""
    ],

    "outlook": "",

    "recommendation": ""
}

Rules:

1. Return ONLY valid JSON.
2. No markdown.
3. No explanations.
4. No extra text.
5. Use values directly from the document.
6. Do NOT invent information.
7. Do NOT assume future plans unless explicitly stated.
8. Do NOT generate risks not mentioned or implied in the document.
9. If information is unavailable use "".
10. company_description <= 100 words.
11. outlook <= 100 words.
12. investment_thesis must contain the top 3 reasons supporting the company.
13. key_highlights must contain the most important business and financial updates.
14. growth_drivers must be based only on information in the document.
15. recommendation must be exactly one of:
    - Positive
    - Neutral
    - Cautious

16. Use concise professional equity research language.

17. Financial metrics mapping:

Revenue can be extracted from:
- Revenue
- Total Revenue
- Income
- Total Income
- Net Revenue
- Operating Revenue
- Revenue from Operations

EBITDA can be extracted from:
- EBITDA
- Adjusted EBITDA
- EBIT
- Operating Profit
- Operating Income

PAT can be extracted from:
- PAT
- Profit After Tax
- Net Profit
- Net Income
- Profit attributable to shareholders

18. If exact Revenue/EBITDA/PAT labels do not exist,
use the closest available equivalent and store the original name in:

source_metric_revenue
source_metric_ebitda
source_metric_pat

19. NEVER return 0 unless the document explicitly reports 0.

20. Prefer current quarter values (Q2 FY26) over annual values when available.

21. All financial figures must match the source document exactly.
"""