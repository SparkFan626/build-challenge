# Build Challenge – Python Solutions

This repository contains solutions for **Assignment 1** and **Assignment 2**, implemented in Python.  
A virtual environment is recommended for consistent execution.

---

## 1. Getting Started

### Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate       # macOS / Linux
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies

This project uses only the Python standard library.  
Still, install from `requirements.txt` for consistency:

```bash
pip install -r requirements.txt
```

---

## 2. Assignment 1 – Producer/Consumer Pattern

### Overview

Assignment 1 implements a simple **Producer–Consumer** workflow using:

- `threading.Thread`
- `queue.Queue` (blocking queue)
- A sentinel value to signal completion
- Unit tests with `unittest`

The producer places items into a shared queue, and the consumer removes them until a sentinel is received.

### Why I used `queue.Queue`

`queue.Queue` internally uses locks and condition variables, so it is safer and more production style than writing a manual wait/notify queue.  
This avoids common deadlock risks and matches real engineering best practices.

### Run Assignment 1

```bash
cd assignment1
python main.py
```

#### Sample Output

The following execution log demonstrates the concurrent behavior of the Producer and Consumer threads. Note that the order of log messages may vary between runs due to concurrency. However, the data is always processed correctly.

```text
Thread-1 - Producing: 1
Thread-1 - Producing: 2
Thread-1 - Producing: 3
Thread-2 - Consumed: 1
Thread-1 - Producing: 4
Thread-2 - Consumed: 2
Thread-1 - Producing: 5
Thread-2 - Consumed: 3
Thread-2 - Consumed: 4
Thread-2 - Consumed: 5
Thread-2 - Consumer received SENTINEL.
Thread-1 - Producer done, SENTINEL sent.

Final Results:
Source data:      [1, 2, 3, 4, 5]
Destination data: [1, 2, 3, 4, 5]
```

### Run tests

```bash
python -m unittest test_producer_consumer.py
```

---

## 3. Assignment 2 – Sales Data Analysis

### Dataset Description

This assignment uses a **Product Sales by Region** dataset (~1,500 rows).  
It includes fields such as:

- Region, Product, Quantity, Unit Price, Total Price  
- Discounts and Promotions  
- Store Location and Payment Method  
- Salesperson  

The dataset is simple but expressive, suitable for demonstrating grouping, filtering, and revenue analysis.

### Approach

The solution implements two programming paradigms:

1.  **Imperative Version:** Utilizes standard control flow like loops and data structures like dictionaries for efficient, stateful processing.
2.  **Functional / Stream Version:** Employs functional programming concepts (`map`, `filter`, `reduce`, `groupby`) to build data processing pipelines.

### Key Analytics Implemented

The application processes the dataset to generate the following business insights:

- Total Sales
- Average Unit Price
- Sales by Region
- Top N Products
- High Value Sales

### Run Assignment 2

```bash
cd assignment2
python main.py
```
#### Sample Output

Running the analysis script produces the following insights.

```text
Loaded rows: 1500

=== Imperative ===
Total sales: 4379992.4285
Average unit price: 298.82694666666663
Sales by region: {'East': 883633.7180000012, 'South': 827768.1869999999, 'North': 967957.9800000007, 'Central': 847153.6845000003, 'West': 853478.8590000002}
Top 3 products by revenue: ['Tablet', 'Laptop', 'Printer']

=== Functional ===
Total sales (FP): 4379992.4284999985
Sales by region (FP): {'Central': 847153.6845, 'East': 883633.718, 'North': 967957.98, 'South': 827768.187, 'West': 853478.8589999999}
High value sales (>1000) grouped by region: {'Central': 804463.632, 'East': 837699.7375, 'North': 930947.592, 'South': 794149.2705, 'West': 822057.5}
```
### Run tests

```bash
python -m unittest test_analysis.py
```

---

## 4. Requirements

```
# This project uses only Python standard library.
# No external packages required.
python>=3.6
```
