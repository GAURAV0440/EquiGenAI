import os
import pandas as pd
import streamlit as st

from src.extractor import DocumentExtractor
from src.analyzer import FinancialAnalyzer
from src.chart_generator import ChartGenerator
from src.pdf_generator import PDFGenerator


st.set_page_config(
    page_title="EquiGenAI",
    page_icon="📈",
    layout="wide"
)

for key in [
    "analysis",
    "chart_path",
    "pdf_path"
]:
    if key not in st.session_state:
        st.session_state[key] = None


with st.sidebar:

    st.title("📈 EquiGenAI")

    st.markdown("""
    ### Features

    ✅ Financial Document Analysis

    ✅ AI-Powered Insights

    ✅ Automated Research Reports

    ✅ PDF Export
    """)


st.title("📈 EquiGenAI")

st.subheader(
    "AI-Powered Equity Research Report Generator"
)

uploaded_file = st.file_uploader(
    "Upload Financial Document",
    type=["pdf", "txt", "csv"]
)

if uploaded_file:

    os.makedirs(
        "data/uploads",
        exist_ok=True
    )

    file_path = os.path.join(
        "data/uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    if st.button(
        "Generate Research Report"
    ):

        try:

            with st.spinner(
                "Analyzing document..."
            ):

                text = (
                    DocumentExtractor.extract(
                        file_path
                    )
                )

                analysis = (
                    FinancialAnalyzer()
                    .analyze(text)
                )

                chart_path = (
                    ChartGenerator()
                    .create_chart(
                        analysis
                    )
                )

                pdf_path = (
                    "outputs/reports/"
                    "equity_report.pdf"
                )

                PDFGenerator().generate(
                    analysis,
                    chart_path,
                    pdf_path
                )

                st.session_state.analysis = analysis
                st.session_state.chart_path = chart_path
                st.session_state.pdf_path = pdf_path

                st.success(
                    "Report Generated Successfully!"
                )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )


if st.session_state.analysis:

    analysis = (
        st.session_state.analysis
    )

    st.header(
        analysis["company_name"]
    )

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            f"Sector: {analysis['sector']}"
        )

    with col2:

        st.success(
            f"Recommendation: {analysis['recommendation']}"
        )

    st.subheader(
        "Company Overview"
    )

    st.write(
        analysis["company_description"]
    )

    st.subheader(
        "Investment Thesis"
    )

    for point in analysis[
        "investment_thesis"
    ]:
        st.markdown(
            f"• {point}"
        )

    st.subheader(
        "Key Highlights"
    )

    for point in analysis[
        "key_highlights"
    ]:
        st.markdown(
            f"• {point}"
        )

    st.subheader(
        "Financial Metrics"
    )

    metrics = analysis[
        "financial_metrics"
    ]

    metrics_df = pd.DataFrame(
        {
            "Metric": [
                "Revenue",
                "Revenue Growth",
                "EBITDA",
                "EBITDA Margin",
                "PAT",
                "PAT Growth"
            ],
            "Value": [
                metrics["revenue"],
                metrics["revenue_growth"],
                metrics["ebitda"],
                metrics["ebitda_margin"],
                metrics["pat"],
                metrics["pat_growth"]
            ]
        }
    )

    st.dataframe(
        metrics_df,
        use_container_width=True,
        hide_index=True
    )

    st.subheader(
        "Financial Performance"
    )

    col1, col2, col3 = st.columns(
        [1, 3, 1]
    )

    with col2:

        st.image(
            st.session_state.chart_path,
            width=800
        )

    st.subheader(
        "Growth Drivers"
    )

    for point in analysis[
        "growth_drivers"
    ]:
        st.markdown(
            f"• {point}"
        )

    st.subheader(
        "Risks"
    )

    for risk in analysis[
        "risks"
    ]:
        st.markdown(
            f"• {risk}"
        )

    st.subheader(
        "Outlook"
    )

    st.write(
        analysis["outlook"]
    )

    with open(
        st.session_state.pdf_path,
        "rb"
    ) as pdf_file:

        st.download_button(
            "📄 Download Research Report",
            data=pdf_file,
            file_name="equity_report.pdf",
            mime="application/pdf"
        )