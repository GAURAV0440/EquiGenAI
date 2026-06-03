import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    Image,
)

from templates.report_template import ReportTemplate


class PDFGenerator:

    def __init__(self):

        self.styles = ReportTemplate.get_styles()

    def generate(
        self,
        analysis_data,
        chart_path,
        output_path,
    ):

        os.makedirs(
            os.path.dirname(output_path),
            exist_ok=True
        )

        pdf = SimpleDocTemplate(
            output_path,
            topMargin=30,
            bottomMargin=30,
            leftMargin=40,
            rightMargin=40
        )

        elements = []

        # Header

        elements.append(
            Paragraph(
                "Retail Equity Research",
                self.styles["Header"]
            )
        )

        elements.append(
            Paragraph(
                analysis_data["company_name"],
                self.styles["CompanyTitle"]
            )
        )

        elements.append(
            Paragraph(
                f"Generated: {datetime.now().strftime('%d %B %Y')}",
                self.styles["Body"]
            )
        )

        elements.append(
            Paragraph(
                f"Sector: {analysis_data['sector']}",
                self.styles["Body"]
            )
        )

        elements.append(
            Spacer(1, 10)
        )

        # Recommendation

        recommendation_table = Table(
            [
                ["Recommendation"],
                [analysis_data["recommendation"]]
            ],
            colWidths=[180]
        )

        recommendation_table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1),
                     colors.lightgreen),
                    ("GRID", (0, 0), (-1, -1),
                     1, colors.black),
                    ("ALIGN", (0, 0), (-1, -1),
                     "CENTER"),
                    ("FONTNAME", (0, 0), (-1, -1),
                     "Helvetica-Bold"),
                ]
            )
        )

        elements.append(
            recommendation_table
        )

        elements.append(
            Spacer(1, 15)
        )

        # Company Overview

        elements.append(
            Paragraph(
                "Company Overview",
                self.styles["SectionHeader"]
            )
        )

        elements.append(
            Paragraph(
                analysis_data["company_description"],
                self.styles["Body"]
            )
        )

        # Investment Thesis

        elements.append(
            Paragraph(
                "Investment Thesis",
                self.styles["SectionHeader"]
            )
        )

        for item in analysis_data["investment_thesis"]:

            elements.append(
                Paragraph(
                    f"• {item}",
                    self.styles["Body"]
                )
            )

        # Financial Metrics

        elements.append(
            Paragraph(
                "Financial Metrics",
                self.styles["SectionHeader"]
            )
        )

        metrics = {
            k: str(v).replace("₹", "Rs.")
            for k, v in analysis_data["financial_metrics"].items()
        }

        table_data = [
            ["Metric", "Value"],
            ["Revenue", metrics["revenue"]],
            ["Revenue Growth", metrics["revenue_growth"]],
            ["EBITDA", metrics["ebitda"]],
            ["EBITDA Margin", metrics["ebitda_margin"]],
            ["PAT", metrics["pat"]],
            ["PAT Growth", metrics["pat_growth"]],
        ]

        table = Table(
            table_data,
            colWidths=[200, 200]
        )

        table.setStyle(
            TableStyle(
                ReportTemplate.table_style()
            )
        )

        elements.append(table)

        elements.append(
            Spacer(1, 10)
        )

        # Outlook

        elements.append(
            Paragraph(
                "Outlook",
                self.styles["SectionHeader"]
            )
        )

        elements.append(
            Paragraph(
                analysis_data["outlook"],
                self.styles["Body"]
            )
        )

        # Page 2

        elements.append(
            PageBreak()
        )

        # Key Highlights

        elements.append(
            Paragraph(
                "Key Highlights",
                self.styles["SectionHeader"]
            )
        )

        for item in analysis_data["key_highlights"]:

            elements.append(
                Paragraph(
                    f"• {item}",
                    self.styles["Body"]
                )
            )

        elements.append(
            Spacer(1, 10)
        )

        # Growth Drivers

        elements.append(
            Paragraph(
                "Growth Drivers",
                self.styles["SectionHeader"]
            )
        )

        for item in analysis_data["growth_drivers"]:

            elements.append(
                Paragraph(
                    f"• {item}",
                    self.styles["Body"]
                )
            )

        elements.append(
            Spacer(1, 10)
        )

        # Chart

        elements.append(
            Paragraph(
                "Financial Performance",
                self.styles["SectionHeader"]
            )
        )

        if os.path.exists(chart_path):

            elements.append(
                Image(
                    chart_path,
                    width=450,
                    height=280
                )
            )

        elements.append(
            Spacer(1, 10)
        )

        # Risks

        elements.append(
            Paragraph(
                "Risks",
                self.styles["SectionHeader"]
            )
        )

        for risk in analysis_data["risks"]:

            elements.append(
                Paragraph(
                    f"• {risk}",
                    self.styles["Body"]
                )
            )

        elements.append(
            Spacer(1, 15)
        )

        elements.append(
            Paragraph(
                "Generated by EquiGenAI",
                self.styles["Body"]
            )
        )

        pdf.build(elements)

        return output_path