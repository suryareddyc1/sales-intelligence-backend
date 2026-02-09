import matplotlib
matplotlib.use("Agg")   # 👈 MUST be before pyplot import

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

CHART_DIR = "data/charts"
os.makedirs(CHART_DIR, exist_ok=True)

def revenue_trend_chart(df: pd.DataFrame):
    df["revenue"] = df["quantity"] * df["price"]
    daily = df.groupby("date")["revenue"].sum()

    plt.figure()
    sns.lineplot(x=daily.index, y=daily.values)
    plt.title("Daily Revenue Trend")
    plt.xlabel("Date")
    plt.ylabel("Revenue")

    path = f"{CHART_DIR}/revenue_trend.png"
    plt.savefig(path)
    plt.close()

    return path
