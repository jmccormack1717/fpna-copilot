import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import pytest
from agent import tools

def test_revenue_vs_budget_runs():
    response, fig = tools.revenue_vs_budget("2025-06")
    assert "Revenue vs Budget" in response
    assert fig is not None

def test_gross_margin_trend_runs():
    response, fig = tools.gross_margin_trend()
    assert "Gross Margin" in response
    assert fig is not None

def test_opex_breakdown_runs():
    response, fig = tools.opex_breakdown("2025-06")
    assert "Opex breakdown" in response
    assert fig is not None

def test_cash_runway_runs():
    response, fig = tools.cash_runway()
    assert "Cash Runway" in response or "indefinite" in response
    # Cash runway may return no chart
