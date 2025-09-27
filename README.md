# FP&A Copilot

A mini CFO Copilot: an AI-powered assistant that answers finance questions from structured CSV data. CFOs can ask about revenue, margins, Opex, and cash runway and get concise, board-ready answers with charts.

---

## Features

- Chatbox interface to ask questions such as:
  - "What was June 2025 revenue vs budget in USD?"
  - "Show Gross Margin % trend for the last 3 months."
  - "Break down Opex by category for June 2025."
  - "What is our current cash runway?"
- Returns answers with inline charts.
- Uses CSV files stored in `fixtures/`:
  - `actuals.csv`, `budget.csv`, `fx.csv`, `cash.csv`
- Metrics implemented:
  - Revenue (USD) vs Budget
  - Gross Margin %
  - Opex total by category
  - EBITDA (proxy)
  - Cash runway

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/jmccormack1717/fpna-copilot
cd fpna-copilot
pip install -r requirements.txt
```

## Running the App
streamlit run app.py

## Running Tests
pytest

## File Structure
<pre>
fpna-copilot/
├── app.py             # Streamlit app
├── agent/             # Planner + tools
│   ├── __init__.py
│   └── tools.py
├── fixtures/          # Dataset CSVs
├── tests/             # Unit tests
├── requirements.txt
└── README.md
</pre>