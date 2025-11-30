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

Two programming paradigms were implemented:

### 1. Imperative Version

- Uses loops and dictionaries  
- Straightforward and commonly used in real-world Python code

### 2. Functional / Stream Version

- Uses `map`, `filter`, `reduce`, and `itertools.groupby`  
- Demonstrates a stream-style pipeline  
- Matches the assignment’s functional programming requirement  

Both approaches generate the same analytical results.

### Implemented analytics

- Total sales  
- Average unit price  
- Sales grouped by region  
- Top N products by revenue  
- High value sales above a threshold  

### Run Assignment 2

```bash
cd assignment2
python main.py
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
