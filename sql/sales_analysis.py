import pandas as pd

df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)

print("\n===== BUSINESS KPIs =====")

print(f"Total Sales: ${df['Sales'].sum():,.2f}")

print(f"Total Profit: ${df['Profit'].sum():,.2f}")

print(f"Total Orders: {df['Order ID'].nunique()}")

print(f"Total Customers: {df['Customer ID'].nunique()}")
print("\n===== SALES BY REGION =====")

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(region_sales)
print("\n===== PROFIT BY REGION =====")

region_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print(region_profit)
print("\n===== SALES BY CATEGORY =====")

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(category_sales)

print("\n===== PROFIT BY CATEGORY =====")

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print(category_profit)
print("\n===== PROFIT BY SUB-CATEGORY =====")

subcategory_profit = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print(subcategory_profit)
print("\n===== TOP 10 CUSTOMERS BY SALES =====")

top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)