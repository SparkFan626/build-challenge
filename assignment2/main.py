# assignment2/main.py

import csv
from analysis import (
    load_data,
    total_sales, total_sales_fp,
    average_unit_price,
    sales_by_region, sales_by_region_fp,
    top_n_products_by_sales,
    high_value_sales_fp,
)


def main():
    # Load CSV data
    filepath = "data/sales.csv"
    with open(filepath, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    data = load_data(rows)
    print("Loaded rows:", len(data))


    # Imperative
    print("\n=== Imperative ===")
    print("Total sales:", total_sales(data))
    print("Average unit price:", average_unit_price(data))
    print("Sales by region:", sales_by_region(data))
    print("Top 3 products by revenue:", top_n_products_by_sales(data, 3))


    # Functional / Stream (FP)
    print("\n=== Functional ===")
    print("Total sales (FP):", total_sales_fp(data))
    print("Sales by region (FP):", sales_by_region_fp(data))

    high_value = high_value_sales_fp(data, threshold=1000)
    print("High value sales (>1000) grouped by region:", high_value)


if __name__ == "__main__":
    main()
