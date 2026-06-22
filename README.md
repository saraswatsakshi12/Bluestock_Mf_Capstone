# Bluestock Fintech — Mutual Fund Analytics Capstone

**Company:** Bluestock Fintech Pvt. Ltd.
**Domain:** Mutual Fund / Fintech
**Duration:** 7 Working Days (~50–55 hours)
**Intern:** Data Analyst Intern — Bluestock Fintech (MJ28)
**Date:** June 2026
**Status:** Complete (Day 1–7) | Release v1.0

---

## Project Overview

An end-to-end Mutual Fund Analytics Platform built on publicly available AMFI India and mfapi.in data. The project covers:

- ETL ingestion of 10 datasets + live NAV from mfapi.in
- Data cleaning and a 5+ table SQLite star schema
- Exploratory data analysis (NAV, AUM, SIP, investor behaviour)
- Performance & risk metrics (CAGR, Sharpe, Sortino, Alpha, Beta, Max Drawdown)
- Advanced risk analytics (VaR, CVaR, rolling Sharpe, investor cohorts, fund recommender)
- An interactive Power BI dashboard (4 pages)
- A final report and presentation summarising findings

> All data is publicly sourced from AMFI India, mfapi.in, NSE/BSE. This project is for educational purposes only and does not constitute financial advice.

---

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/bluestock-mf-capstone.git
cd bluestock-mf-capstone
```

### 2. Create virtual environment & install dependencies
```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Place datasets in `data/raw/`
Download the 10 CSV datasets from the project's shared Google Drive folder and place them in `data/raw/`:

```
data/raw/01_fund_master.csv
data/raw/02_nav_history.csv
data/raw/03_aum_by_fund_house.csv
data/raw/04_monthly_sip_inflows.csv
data/raw/05_category_inflows.csv
data/raw/06_industry_folio_count.csv
data/raw/07_scheme_performance.csv
data/raw/08_investor_transactions.csv
data/raw/09_portfolio_holdings.csv
data/raw/10_benchmark_indices.csv
```

### 4. Run the full pipeline
```bash
python run_pipeline.py
```
This runs ingestion → cleaning → database load → performance metrics → risk analytics in sequence and prints a stage-by-stage status summary.

### 5. Run individual stages (optional)
```bash
python scripts/data_ingestion.py        # Load & inspect all 10 CSVs
python scripts/live_nav_fetch.py        # Fetch live NAV from mfapi.in
python scripts/recommender.py           # Interactive fund recommendation by risk appetite
```

### 6. Open the dashboard
Open `dashboard/bluestock_mf_dashboard.pbix` in Power BI Desktop, or view the static export at `dashboard/Dashboard.pdf`.

---

## Folder Structure

```
bluestock_mf_capstone/
├── data/
│   ├── raw/                  ← Original downloaded / API-fetched files
│   ├── processed/            ← Cleaned, merged CSVs (fund_scorecard.csv, alpha_beta.csv, var_cvar_report.csv, etc.)
│   └── db/                   ← bluestock_mf.db (SQLite database)
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
├── scripts/
│   ├── data_ingestion.py     ← Load & inspect all 10 CSVs
│   ├── live_nav_fetch.py     ← mfapi.in live NAV fetcher
│   ├── data_cleaning.py      ← Cleaning & validation logic
│   ├── load_to_sqlite.py     ← Loads cleaned data into SQLite
│   ├── compute_metrics.py    ← CAGR, Sharpe, Sortino, Alpha, Beta, Max DD
│   ├── risk_metrics.py       ← VaR, CVaR, rolling Sharpe, cohort analysis
│   ├── recommender.py        ← Risk-based fund recommendation model
│   └── generate_report_charts.py / generate_supporting_data.py
├── sql/
│   ├── schema.sql            ← CREATE TABLE statements (star schema)
│   └── queries.sql           ← 10 analytical queries
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   ├── Dashboard.pdf
│   └── page1.png … page4.png
├── reports/
│   ├── charts/                ← All EDA & analytics PNG charts
│   ├── data_quality_report_day1.txt
│   ├── Final_Report.pdf
│   └── Bluestock_MF_Presentation.pptx
├── run_pipeline.py            ← Master ETL + analytics orchestrator
├── requirements.txt
└── README.md
```

---

## Data Sources

| Source | URL | Data |
|--------|-----|------|
| AMFI India | amfiindia.com | NAV, AUM, Folio, SIP |
| mfapi.in | api.mfapi.in/mf/{code} | Historical NAV (JSON) |
| NSE India | nseindia.com | Benchmark Index Prices |
| BSE India | bseindia.com | BSE SmallCap Index |

---

## 7-Day Task Summary

| Day | Focus | Status | Key Deliverables |
|-----|-------|--------|-------------------|
| 1 | Project Setup + Data Ingestion | ✅ Done | `data_ingestion.py`, `live_nav_fetch.py`, `requirements.txt` |
| 2 | Data Cleaning + SQL DB Design | ✅ Done | `bluestock_mf.db`, `schema.sql`, `queries.sql` |
| 3 | Exploratory Data Analysis | ✅ Done | `EDA_Analysis.ipynb` with 15+ charts |
| 4 | Fund Performance Analytics | ✅ Done | `fund_scorecard.csv`, `alpha_beta.csv` |
| 5 | Dashboard Development | ✅ Done* | `bluestock_mf_dashboard.pbix`, `Dashboard.pdf` |
| 6 | Advanced Analytics + Risk | ✅ Done | `var_cvar_report.csv`, `recommender.py` |
| 7 | Final Report + Deployment | ✅ Done | `Final_Report.pdf`, `Bluestock_MF_Presentation.pptx` |

\* Built in Power BI Desktop after the web/online version proved limited for relationship modelling and PDF/PNG export.

---

## Key Metrics Computed

- **CAGR** — 1yr, 3yr, 5yr compound annual growth rates
- **Sharpe Ratio** — Risk-adjusted return (Rf = 6.5% RBI repo rate proxy)
- **Sortino Ratio** — Downside-risk-adjusted return
- **Alpha & Beta** — OLS regression of fund returns vs Nifty 100
- **Max Drawdown** — Worst peak-to-trough NAV decline
- **VaR (95%) & CVaR** — Historical Value at Risk and Conditional VaR
- **HHI** — Herfindahl-Hirschman sector concentration index
- **Fund Scorecard** — Composite 0–100 score (30% 3yr return, 25% Sharpe, 20% Alpha, 15% expense ratio inverse, 10% Max DD inverse)

---

## Dashboard

The Power BI dashboard (`dashboard/bluestock_mf_dashboard.pbix`) has 4 pages:

1. **Industry Overview** — KPI cards (Total AUM, SIP Inflows, Folios, Schemes), AUM by fund house, industry AUM trend
2. **Fund Performance** — Return vs risk scatter, sortable fund scorecard, NAV vs benchmark line chart
3. **Investor Analytics** — Transaction amount by state, SIP/Lumpsum/Redemption split, age group analysis
4. **SIP & Market Trends** — SIP inflow vs Nifty 50 dual-axis, category inflow heatmap

Each page includes Fund House / Category / Date Range / State slicers.

> **Note:** Power BI Online (web) does not support full relationship modelling, drill-through, or PDF/PNG export — these require Power BI **Desktop**. If you only have web access, treat `Dashboard.pdf` and the page screenshots as the canonical Day 5 deliverable, with the `.pbix` available once opened in Desktop.

---

## Git Workflow

```bash
git add .
git commit -m "Final: Complete Bluestock MF Capstone"
git tag v1.0
git push origin main
git push origin v1.0
```

---

## Limitations

- NAV and AUM datasets are anchored to real AMFI/mfapi.in values but extrapolated using simulated volatility for dates outside the anchor points.
- Investor transaction data is synthetically generated, though calibrated to realistic Indian MF demographic and geographic distributions.
- Benchmark selection (Nifty 50/100) materially affects Alpha and Beta results; a different benchmark would shift rankings.
- This is a 1-week individual capstone — risk models (VaR, Sharpe) use simplified assumptions (e.g. constant risk-free rate) rather than a full term structure.

---

## License

Educational use only. Data sourced from AMFI India (public). Not financial advice.
