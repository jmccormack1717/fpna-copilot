import pandas as pd
import matplotlib.pyplot as plt

# Load datasets from fixtures
actuals = pd.read_csv("fixtures/actuals.csv")
budget = pd.read_csv("fixtures/budget.csv")
cash = pd.read_csv("fixtures/cash.csv")
fx = pd.read_csv("fixtures/fx.csv")

def revenue_vs_budget(month: str):
    actual_rev = actuals[(actuals["month"] == month) & (actuals["account_category"] == "Revenue")]["amount"].sum()
    budget_rev = budget[(budget["month"] == month) & (budget["account_category"] == "Revenue")]["amount"].sum()

    fig, ax = plt.subplots()
    ax.bar(["Actual", "Budget"], [actual_rev, budget_rev], color=["blue", "orange"])
    ax.set_title(f"Revenue vs Budget ({month})")
    ax.set_ylabel("Amount")

    response = f"Revenue vs Budget for {month}: Actual = {actual_rev:,.0f}, Budget = {budget_rev:,.0f}"

    return response, fig


def gross_margin_trend():
    rev = actuals[actuals["account_category"] == "Revenue"].groupby("month")["amount"].sum()
    cogs = actuals[actuals["account_category"] == "COGS"].groupby("month")["amount"].sum()
    df = pd.DataFrame({"Revenue": rev, "COGS": cogs})
    df["GrossMarginPct"] = (df["Revenue"] - df["COGS"]) / df["Revenue"]

    last3 = df.tail(3)

    fig, ax = plt.subplots()
    ax.plot(last3.index, last3["GrossMarginPct"], marker="o", linestyle="-")
    ax.set_title("Gross Margin % (Last 3 Months)")
    ax.set_ylabel("Gross Margin %")

    response = "Gross Margin % trend for the last 3 months shown below."

    return response, fig


def opex_breakdown(month: str):
    df = actuals[(actuals["month"] == month) & (actuals["account_category"].str.startswith("Opex:"))]
    opex_by_cat = df.groupby("account_category")["amount"].sum()

    fig, ax = plt.subplots()
    opex_by_cat.plot(kind="bar", ax=ax)
    ax.set_title(f"Opex Breakdown ({month})")
    ax.set_ylabel("Amount")

    response = f"Opex breakdown for {month} shown below."

    return response, fig


def cash_runway():
    rev = actuals[actuals["account_category"] == "Revenue"].groupby("month")["amount"].sum()
    cogs = actuals[actuals["account_category"] == "COGS"].groupby("month")["amount"].sum()
    opex = actuals[actuals["account_category"].fillna("").str.startswith("Opex:")].groupby("month")["amount"].sum()

    df = pd.DataFrame({"Revenue": rev, "COGS": cogs, "Opex": opex}).sort_index()
    df["NetBurn"] = df["COGS"] + df["Opex"] - df["Revenue"]

    last3 = df["NetBurn"].tail(3)
    avg_burn = last3.mean()

    current_cash = cash.sort_values("month", ascending=False).iloc[0]["cash_usd"]

    if avg_burn <= 0:
        response = "No cash burn in the last 3 months. Cash runway is indefinite."
        return response, None

    runway_months = current_cash / avg_burn
    response = f"Cash Runway: {runway_months:.1f} months (Current cash = ${current_cash:,.0f}, Avg monthly net burn = ${avg_burn:,.0f})"

    return response, None



def handle_question(question: str):
    """
    Routes a question to the appropriate tool.
    Uses fixed month '2025-06' for month-specific metrics.
    """
    q = question.lower()

    if "revenue" in q and "budget" in q:
        return revenue_vs_budget("2025-06")

    elif "gross margin" in q:
        return gross_margin_trend()

    elif "opex" in q:
        return opex_breakdown("2025-06")

    elif "cash" in q:
        return cash_runway()

    else:
        return "Sorry, I don't understand that question yet.", None
