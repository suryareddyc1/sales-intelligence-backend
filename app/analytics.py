import pandas as pd


def dashboard_summary(df: pd.DataFrame):
    df["revenue"] = df["quantity"] * df["price"]
    df["profit"] = df["quantity"] * (df["price"] - df["cost"])

    return {
        "total_revenue": int(df["revenue"].sum()),
        "total_profit": int(df["profit"].sum()),
        "best_product": df.groupby("product")["revenue"].sum().idxmax(),
        "avg_daily_revenue": int(df.groupby("date")["revenue"].sum().mean())
    }


def top_products(df: pd.DataFrame):
    df["revenue"] = df["quantity"] * df["price"]

    result = (
        df.groupby("product")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    return result.to_dict()


def category_performance(df: pd.DataFrame):
    df["revenue"] = df["quantity"] * df["price"]
    df["profit"] = df["quantity"] * (df["price"] - df["cost"])

    result = df.groupby("category").agg({
        "revenue": "sum",
        "profit": "sum"
    })

    return result.reset_index().to_dict(orient="records")


def inventory_alerts(df: pd.DataFrame):
    alerts = []

    rolling = (
        df.groupby("product")["quantity"]
        .rolling(window=7)
        .mean()
        .reset_index()
    )

    for _, row in rolling.iterrows():
        if row["quantity"] < 5:
            alerts.append({
                "product": row["product"],
                "message": "Low demand detected"
            })

    return alerts
