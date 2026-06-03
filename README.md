# EquiGenAI 📈

AI-Powered Equity Research Report Generator

## Overview

EquiGenAI is an AI-powered application that automatically generates equity research reports from company financial documents.

Instead of manually reading lengthy annual reports, earnings presentations, or financial statements, users can upload a document and receive a structured equity research report containing:

* Company Overview
* Investment Thesis
* Key Highlights
* Financial Metrics
* Growth Drivers
* Risks
* Future Outlook
* Investment Recommendation
* Financial Performance Charts
* Downloadable PDF Report

The project uses Google's Gemini API to analyze financial documents and generate professional research insights.

---

## Problem Statement

Financial reports and investor presentations are often lengthy and time-consuming to analyze.

Investors, students, and analysts spend significant effort extracting important information such as:

* Revenue
* EBITDA
* Profit After Tax (PAT)
* Growth Drivers
* Risks
* Future Outlook

This project automates that process and converts raw financial documents into easy-to-understand research reports.

---

## Features

✅ Upload PDF, TXT, or CSV financial documents

✅ Extract document content automatically

✅ AI-powered financial analysis using Gemini

✅ Generate structured equity research reports

✅ Create financial performance charts

✅ Generate downloadable PDF reports

✅ Interactive Streamlit web application

---

## Tech Stack

### Frontend

* Streamlit

### AI Model

* Google Gemini 2.5 Flash

### Data Processing

* Python
* Pandas
* PyMuPDF (fitz)

### Visualization

* Matplotlib

### PDF Generation

* ReportLab

---

## Project Structure

```text
EquiGenAI/
│
├── src/
│   ├── analyzer.py
│   ├── chart_generator.py
│   ├── extractor.py
│   ├── pdf_generator.py
│   └── prompts.py
│
├── templates/
│   └── report_template.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Workflow

### Step 1: Upload Financial Document

The user uploads a company financial document in:

* PDF
* TXT
* CSV

format.

### Step 2: Extract Text

The Document Extractor extracts content from the uploaded file.

### Step 3: AI Analysis

The extracted text is sent to Gemini API using a carefully designed prompt.

Gemini returns structured JSON containing:

* Company Details
* Financial Metrics
* Growth Drivers
* Risks
* Outlook
* Recommendation

### Step 4: Chart Generation

Financial metrics such as:

* Revenue
* EBITDA
* PAT

are converted into visual charts using Matplotlib.

### Step 5: PDF Report Generation

A professional equity research report is generated using ReportLab.

### Step 6: Download Report

Users can download the generated report as a PDF.

---

## Challenges Faced

### 1. JSON Parsing Issues

Initially, Gemini sometimes returned responses wrapped in markdown code blocks.

Example:

```json
{
   ...
}
```

This caused JSON parsing failures.

Solution:

* Added response cleaning before parsing.
* Improved prompt instructions to force valid JSON output.

---

### 2. Financial Number Extraction

Financial values appeared in different formats:

* ₹ 5,361 Cr
* Rs. 5,361 Cr
* 5,361

This created chart generation errors.

Solution:

* Implemented a number cleaning function to standardize values.

---

### 3. Chart Display Size

The chart initially occupied the entire Streamlit page and looked oversized.

Solution:

* Adjusted chart dimensions.
* Centered charts using Streamlit columns.
* Used different sizing for UI and PDF.

---

### 4. PDF Formatting

Large sections and charts caused layout issues.

Solution:

* Improved spacing.
* Added page breaks.
* Created reusable report templates.

---

### 5. GitHub Security

The project uses Gemini API keys stored in `.env`.

Challenge:

* Prevent accidental exposure of API keys.

Solution:

* Configured `.gitignore`.
* Excluded:

  * `.env`
  * `.venv`
  * outputs
  * uploaded documents

from GitHub.

---

## Sample Output

The generated report includes:

* Company Overview
* Investment Thesis
* Financial Metrics Table
* Financial Charts
* Growth Drivers
* Risks
* Outlook
* Investment Recommendation

along with a downloadable PDF report.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/GAURAV0440/EquiGenAI.git
```

Move into the project folder:

```bash
cd EquiGenAI
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

Linux/Mac:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
MODEL_NAME=gemini-2.5-flash
```

Run the application:

```bash
streamlit run app.py
```

---

## Future Improvements

* Multi-company comparison
* Stock valuation models
* Sentiment analysis
* Interactive dashboards
* Historical trend analysis
* Export to Excel and PowerPoint
* More advanced visualizations

---

## Learning Outcomes

Through this project, I learned:

* Prompt engineering
* Gemini API integration
* Financial document analysis
* PDF generation using ReportLab
* Data visualization using Matplotlib
* Streamlit application development
* Git and GitHub workflow
* Secure handling of API keys

---

## Author

Gaurav Chawla

Built as part of a Financial AI and Equity Research Automation project.
