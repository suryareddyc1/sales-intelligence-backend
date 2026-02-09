from fastapi import FastAPI, UploadFile, File
import pandas as pd
from app.analytics import (
    dashboard_summary,
    top_products,
    category_performance,
    inventory_alerts
)
from app.charts import revenue_trend_chart
from fastapi.responses import FileResponse

app = FastAPI(title="Small Business Sales Intelligence API")

DATA_PATH = "data/sales.csv"


@app.post("/upload-sales")
async def upload_sales(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    df.to_csv(DATA_PATH, index=False)
    return {"message": "Sales data uploaded successfully"}


@app.get("/dashboard-summary")
def get_dashboard_summary():
    df = pd.read_csv(DATA_PATH)
    return dashboard_summary(df)


@app.get("/top-products")
def get_top_products():
    df = pd.read_csv(DATA_PATH)
    return top_products(df)


@app.get("/category-performance")
def get_category_performance():
    df = pd.read_csv(DATA_PATH)
    return category_performance(df)


@app.get("/inventory-alerts")
def get_inventory_alerts():
    df = pd.read_csv(DATA_PATH)
    return inventory_alerts(df)


@app.get("/charts/revenue-trend")
def get_revenue_trend_chart():
    df = pd.read_csv(DATA_PATH)
    path = revenue_trend_chart(df)
    return {"chart_path": path}

@app.get("/charts/revenue-trend")
def get_revenue_trend_chart():
    df = pd.read_csv(DATA_PATH)
    path = revenue_trend_chart(df)
    return FileResponse(path, media_type="image/png")