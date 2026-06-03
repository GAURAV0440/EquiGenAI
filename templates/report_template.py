from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


class ReportTemplate:

    PRIMARY = colors.HexColor("#00897B")
    DARK = colors.HexColor("#004D40")
    LIGHT = colors.HexColor("#E0F2F1")

    @staticmethod
    def get_styles():

        styles = getSampleStyleSheet()

        styles.add(
            ParagraphStyle(
                name="CompanyTitle",
                fontSize=24,
                leading=28,
                textColor=ReportTemplate.DARK,
                spaceAfter=10,
            )
        )

        styles.add(
            ParagraphStyle(
                name="Header",
                fontSize=20,
                leading=24,
                textColor=ReportTemplate.PRIMARY,
                spaceAfter=12,
            )
        )

        styles.add(
            ParagraphStyle(
                name="SectionHeader",
                fontSize=15,
                leading=18,
                textColor=ReportTemplate.PRIMARY,
                spaceBefore=8,
                spaceAfter=6,
            )
        )

        styles.add(
            ParagraphStyle(
                name="Body",
                fontSize=10,
                leading=14,
            )
        )

        return styles

    @staticmethod
    def table_style():

        return [
            ("BACKGROUND", (0, 0), (-1, 0), ReportTemplate.PRIMARY),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1),
             [colors.white, ReportTemplate.LIGHT]),
        ]