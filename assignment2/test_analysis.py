# assignment2/test_analysis.py

import unittest
from analysis import (
    total_sales, total_sales_fp,
    average_unit_price,
    sales_by_region, sales_by_region_fp,
    top_n_products_by_sales,
    high_value_sales_fp
)


class TestSalesAnalysis(unittest.TestCase):

    def setUp(self):
        self.data = [
            {"Region": "East", "Product": "Laptop", "UnitPrice": 100, "TotalPrice": 1000},
            {"Region": "East", "Product": "Desk",   "UnitPrice": 200, "TotalPrice": 2000},
            {"Region": "West", "Product": "Laptop", "UnitPrice": 150, "TotalPrice": 1500},
        ]

    # Basic versions
    def test_total_sales(self):
        self.assertEqual(total_sales(self.data), 4500)

    def test_average_unit_price(self):
        self.assertEqual(average_unit_price(self.data), (100 + 200 + 150) / 3)

    def test_sales_by_region(self):
        result = sales_by_region(self.data)
        self.assertEqual(result["East"], 3000)
        self.assertEqual(result["West"], 1500)

    def test_top_products(self):
        result = top_n_products_by_sales(self.data, 1)
        self.assertEqual(result, ["Laptop"])

    # FP versions 
    def test_total_sales_fp(self):
        self.assertEqual(total_sales_fp(self.data), 4500)

    def test_sales_by_region_fp(self):
        result = sales_by_region_fp(self.data)
        self.assertEqual(result["East"], 3000)
        self.assertEqual(result["West"], 1500)

    def test_high_value_sales_fp(self):
        result = high_value_sales_fp(self.data, threshold=1200)
        self.assertEqual(result["East"], 2000)
        self.assertEqual(result["West"], 1500)


if __name__ == "__main__":
    unittest.main()
