# Feedback-Sentiment-Dashboard
Feedback Sentiment Dashboard is a lightweight, Python-based mobile analytics application developed to help businesses, NGOs, and institutions collect, analyze, and interpret customer or client feedback using sentiment analysis.  Designed specifically for field deployment in low-infrastructure environments (e.g. Malawi).

It is a Python-based, mobile-compatible analytics tool for processing and visualizing customer or user feedback using sentiment analysis. It is built to help organizations interpret qualitative feedback data, monitor satisfaction levels, and identify recurring issues through intelligent automation and visualization.

The application is optimized for offline use in environments with limited internet access. It supports CSV-based data import, rule-based and machine learning sentiment classification, and visual summary dashboards.

---

## Features

- Mobile-friendly interface built using Kivy and KivyMD
- Upload and analyze feedback via CSV files
- Sentiment classification: Positive, Neutral, Negative
- Rule-based and ML-based sentiment analysis using NLP libraries
- Dashboard summaries with charts and metric breakdowns
- Identification of common keywords and issue clusters
- Exportable reports for stakeholders or management

---

## Tech Stack

- **Python 3.10+**
- **Kivy / KivyMD** – Cross-platform mobile UI
- **Pandas** – Data management and transformation
- **TextBlob / Scikit-learn** – Sentiment analysis and ML classification
- **Matplotlib / Plotly** – Data visualization
- **NLTK / spaCy** (optional) – Advanced NLP support

---

## Use Cases

- Monitor customer satisfaction trends over time
- Track and categorize recurring complaints or praise
- Support customer service strategy through evidence-based insights
- Provide feedback summaries to stakeholders
- Collect real-time field data for analysis (offline or online)

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/feedback-sentiment-dashboard.git
cd feedback-sentiment-dashboard

Create and activate a virtual environment

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install Python dependencies

bash
Copy code
pip install -r requirements.txt
Run the app

bash
Copy code
python main.py
Directory Structure
graphql
Copy code
feedback-sentiment-dashboard/
│
├── assets/                     # App assets (icons, images, etc.)
├── data/                       # Uploaded feedback files
├── models/                     # ML models and sentiment logic
├── screens/                    # Kivy screen layouts
├── components/                 # Reusable UI components
├── utils/                      # NLP processing and helpers
├── main.py                     # App entry point
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
Requirements
List of primary packages required (included in requirements.txt):

kivy

kivymd

pandas

matplotlib

plotly

textblob

scikit-learn

nltk

spacy (optional for extended NLP tasks)

How Sentiment Analysis Works
The system uses two modes of sentiment classification:

Rule-Based (Default)
Uses TextBlob to compute polarity scores and determine sentiment labels:

Polarity > 0.1: Positive

Polarity between -0.1 and 0.1: Neutral

Polarity < -0.1: Negative

Machine Learning (Optional)
A pre-trained logistic regression classifier can be used to improve sentiment accuracy based on domain-specific feedback datasets. Training scripts are included under /models.

Output Reports
Sentiment breakdown: % Positive / Neutral / Negative

Keyword frequency: most common terms per sentiment class

Visual charts: bar, pie, and trend lines

Optional export: CSV, PDF (coming soon)

License
This project is licensed under the MIT License. See LICENSE file for details.

Contributions
Feel free to fork, improve, or adapt this tool for your own feedback analysis use case. Pull requests are welcome.
