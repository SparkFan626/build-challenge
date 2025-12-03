# assignment2/test_analysis.py

import unittest
from analysis import (
    total_sales, total_sales_fp,
    sales_by_region, sales_by_region_fp,
    high_value_sales, high_value_sales_fp
)

class TestSalesAnalysis(unittest.TestCase):

    def setUp(self):
        self.data = [
            {"Region": "East", "Product": "Laptop", "UnitPrice": 100, "TotalPrice": 1000},
            {"Region": "East", "Product": "Desk",   "UnitPrice": 200, "TotalPrice": 2000},
            {"Region": "West", "Product": "Laptop", "UnitPrice": 150, "TotalPrice": 1500},
        ]

    # Pair 1: Total Sales
    def test_total_sales_imperative(self):
        self.assertEqual(total_sales(self.data), 4500)

    def test_total_sales_fp(self):
        self.assertEqual(total_sales_fp(self.data), 4500)

    # Pair 2: Sales by Region
    def test_sales_by_region_imperative(self):
        result = sales_by_region(self.data)
        self.assertEqual(result["East"], 3000)
        self.assertEqual(result["West"], 1500)

    def test_sales_by_region_fp(self):
        result = sales_by_region_fp(self.data)
        self.assertEqual(result["East"], 3000)
        self.assertEqual(result["West"], 1500)

    # Pair 3: High Value Sales (> 1000)
    def test_high_value_sales_imperative(self):
        # Should exclude the item with exactly 1000
        result = high_value_sales(self.data, threshold=1000)
        self.assertEqual(result["East"], 2000)
        self.assertEqual(result["West"], 1500)

    def test_high_value_sales_fp(self):
        result = high_value_sales_fp(self.data, threshold=1000)
        self.assertEqual(result["East"], 2000)
        self.assertEqual(result["West"], 1500)


if __name__ == "__main__":
    unittest.main()