import pandas as pd
from datetime import datetime

def load_data(filepath):
    """Load CSV data and return a pandas DataFrame."""
    df = pd.read_csv(filepath, parse_dates=["date"])
    return df

def generate_summary(df):
    """
    Generate key business metrics from the DataFrame.
    Return a dict of summary statistics.
    """

    summary = {
        "total_revenue": df["revenue"].sum(),
        "total_units": df["units_sold"].sum(),
        "avg_revenue_per_day": df.groupby("date")["revenue"].sum().mean(),
        "top_product": df.groupby("product")["revenue"].sum().idxmax(),
        "top_region": df.groupby("region")["revenue"].sum().idxmax(),
        "report_date": datetime.now().strftime("%B %d, %Y at %H:%M")
    }
    return summary

def generate_product_table(df):
    """Create a pre-product breakdown as an HTML table."""

    product_summary = (
        df.groupby("product")
        .agg(
            Total_Revenue=("revenue", "sum"),
            Total_Units=("units_sold", "sum"),
            Avg_Revenue=("revenue", "mean"),
        )
        .reset_index()
        .sort_values("Total_Revenue", ascending=False)
    )
    product_summary["Total_Revenue"] = product_summary["Total_Revenue"].apply(
        lambda x: f"₹{x:,.0f}"
    )
    product_summary["Avg_Revenue"] = product_summary["Avg_Revenue"].apply(
        lambda x: f"₹{x:,.0f}"
    )
    return product_summary.to_html(index=False, border=0, classes="data-table")

def generate_region_table(df):
    """Create a pre-region breakdown as an HTML table."""

    region_summary = (
        df.groupby("region")
        .agg(
            Total_Revenue=("revenue", "sum"),
            Total_Units=("units_sold", "sum"),
        )
        .reset_index()
        .sort_values("Total_Revenue", ascending=False)
    )
    region_summary["Total_Revenue"] = region_summary["Total_Revenue"].apply(
        lambda x: f"₹{x:,.0f}"
    )
    return region_summary.to_html(index=False, border=0, classes="data-table")

def build_html_report(df, output_path="report.html"):
    """
    Combine summary + tables into a full HTML email report.
    Also saves the HTML to a file for preview.
    """

    summary = generate_summary(df)
    product_table = generate_product_table(df)
    region_table = generate_region_table(df)

    html = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Sales Performance Report</title>

  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 20px;
      color: #333;
      background-color: #f9f9f9;
    }}

    .container {{
      max-width: 800px;
      margin: auto;
      background: #fff;
      padding: 20px;
      border-radius: 8px;
    }}

    h1 {{
      text-align: center;
      color: #2c3e50;
    }}

    h2 {{
      margin-top: 25px;
      color: #34495e;
      border-bottom: 1px solid #eee;
      padding-bottom: 5px;
    }}

    .metric {{
      margin: 10px 0;
      font-size: 16px;
    }}

    .highlight {{
      margin: 5px 0;
    }}

    .footer {{
      margin-top: 30px;
      text-align: center;
      font-size: 12px;
      color: #888;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
    }}

    table th, table td {{
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }}

    table th {{
      background-color: #f2f2f2;
    }}
  </style>
</head>

<body>
  <div class="container">

    <h1>📊 Sales Performance Report</h1>

    <p style="text-align:center; color:#777;">
      Generated on {summary['report_date']}
    </p>

    <h2>📈 Key Metrics</h2>

    <div class="metric"><strong>Total Revenue:</strong> ₹{summary['total_revenue']:,.0f}</div>
    <div class="metric"><strong>Total Units Sold:</strong> {summary['total_units']:,}</div>
    <div class="metric"><strong>Avg Daily Revenue:</strong> ₹{summary['avg_revenue_per_day']:,.0f}</div>

    <h2>Highlights</h2>

    <div class="highlight"><strong>Top Product:</strong> {summary['top_product']}</div>
    <div class="highlight"><strong>Top Region:</strong> {summary['top_region']}</div>

    <h2>Product Breakdown</h2>
    {product_table}

    <h2>Region Breakdown</h2>
    {region_table}

    <div class="footer">
      Automated Email Report · Project 03/100 · Python Portfolio
    </div>

  </div>
</body>
</html>
"""
    
