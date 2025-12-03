# assignment2/analysis.py

from typing import List, Dict, Any
from collections import defaultdict
from functools import reduce
from itertools import groupby


# Data Loading
def safe_float(val):
    """Convert value to float safely; return 0 on failure."""
    try:
        return float(val)
    except:
        return 0.0

def load_data(csv_rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Convert numeric fields in CSV rows to floats.
    """
    numeric_fields = ["Quantity", "UnitPrice", "TotalPrice", "ShippingCost"]

    for row in csv_rows:
        for f in numeric_fields:
            if f in row:
                row[f] = safe_float(row.get(f))
    return csv_rows


# Imperative Version
def total_sales(data: List[Dict[str, Any]]) -> float:
    """
    Sum of TotalPrice across all rows.
    """
    total = 0.0
    for row in data:
        total += row["TotalPrice"]
    return total

def sales_by_region(data: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Group by region and sum sales.
    """
    result = defaultdict(float)
    for row in data:
        result[row["Region"]] += row["TotalPrice"]
    return dict(result)

def high_value_sales(data: List[Dict[str, Any]], threshold: float) -> Dict[str, float]:
    """
    Filter sales > threshold, then group by region.
    """
    result = defaultdict(float)
    for row in data:
        if row["TotalPrice"] > threshold:
            result[row["Region"]] += row["TotalPrice"]
    return dict(result)


# Functional / Stream Version
def total_sales_fp(data: List[Dict[str, Any]]) -> float:
    """
    Use map + reduce to sum TotalPrice.
    """
    prices = map(lambda r: r["TotalPrice"], data)
    return reduce(lambda a, b: a + b, prices, 0.0)

def sales_by_region_fp(data: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    FP pipeline: sort -> group -> sum.
    """
    sorted_data = sorted(data, key=lambda x: x["Region"])
    return {
        region: sum(map(lambda r: r["TotalPrice"], group))
        for region, group in groupby(sorted_data, key=lambda x: x["Region"])
    }

def high_value_sales_fp(data: List[Dict[str, Any]], threshold: float) -> Dict[str, float]:
    """
    FP pipeline: filter -> sort -> group -> sum.
    """
    filtered = filter(lambda r: r["TotalPrice"] > threshold, data)
    sorted_data = sorted(filtered, key=lambda x: x["Region"])

    return {
        region: sum(map(lambda r: r["TotalPrice"], group))
        for region, group in groupby(sorted_data, key=lambda x: x["Region"])
    }
