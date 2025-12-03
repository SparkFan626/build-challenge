# assignment2/main.py

import csv
from analysis import (
    load_data,
    # Pair 1: Aggregation
    total_sales, total_sales_fp,
    # Pair 2: Grouping
    sales_by_region, sales_by_region_fp,
    # Pair 3: Filtering + Grouping
    high_value_sales, high_value_sales_fp
)


def main():
    # Load CSV data
    filepath = "data/sales.csv"
    with open(filepath, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    data = load_data(rows)
    print("Loaded rows:", len(data))


    # Imperative 
    print("\n=== Imperative Version===")
    print("Total sales:", total_sales(data))
    print("Sales by Region:", sales_by_region(data))
    
    high_value = high_value_sales(data, threshold=1000)
    print("High value sales (>1000) grouped by region:", high_value)


    # Functional / Stream (FP)
    print("\n=== Functional Version===")
    print("Total sales:", total_sales_fp(data))
    print("Sales by region:", sales_by_region_fp(data))

    high_value_fp = high_value_sales_fp(data, threshold=1000)
    print("High value sales (>1000) grouped by region:", high_value_fp)


if __name__ == "__main__":
    main()
