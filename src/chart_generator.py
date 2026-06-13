import os
import matplotlib.pyplot as plt


class ChartGenerator:

    @staticmethod
    def clean_number(value):

        if value is None:
            return 0.0

        value = str(value).strip()

        multiplier = 1

        value_lower = value.lower()

        if "bn" in value_lower or "billion" in value_lower:
            multiplier = 1000

        value = (
            value
            .replace("₹", "")
            .replace("Rs.", "")
            .replace("rs.", "")
            .replace("Cr", "")
            .replace("cr", "")
            .replace("Crore", "")
            .replace("crore", "")
            .replace("Mn", "")
            .replace("mn", "")
            .replace("Million", "")
            .replace("million", "")
            .replace("Bn", "")
            .replace("bn", "")
            .replace("Billion", "")
            .replace("billion", "")
            .replace(",", "")
            .replace("%", "")
            .strip()
        )

        try:
            return float(value) * multiplier

        except Exception:
            print(f"Failed to convert: {value}")
            return 0.0

    @classmethod
    def create_chart(cls, data):

        os.makedirs(
            "outputs/charts",
            exist_ok=True
        )

        metrics_data = data.get(
            "financial_metrics",
            {}
        )

        revenue = cls.clean_number(
            metrics_data.get(
                "revenue",
                0
            )
        )

        ebitda = cls.clean_number(
            metrics_data.get(
                "ebitda",
                0
            )
        )

        pat = cls.clean_number(
            metrics_data.get(
                "pat",
                0
            )
        )

        metrics = [
            "Revenue",
            "EBITDA",
            "PAT"
        ]

        values = [
            revenue,
            ebitda,
            pat
        ]

        plt.figure(
            figsize=(10, 6)
        )

        bars = plt.bar(
            metrics,
            values
        )

        plt.title(
            f"{data.get('company_name', 'Company')} Financial Performance"
        )

        plt.ylabel(
            "₹ Crore"
        )

        plt.grid(
            axis="y",
            linestyle="--",
            alpha=0.4
        )

        for bar, value in zip(
            bars,
            values
        ):

            plt.text(
                bar.get_x()
                + bar.get_width() / 2,
                value,
                f"{value:,.0f}",
                ha="center",
                va="bottom"
            )

        plt.tight_layout()

        chart_path = (
            "outputs/charts/"
            "financial_comparison.png"
        )

        plt.savefig(
            chart_path,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        return chart_path