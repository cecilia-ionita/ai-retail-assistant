# AI Retail Assistant

AI Retail Assistant is a Python portfolio project that processes retail order data and transforms it into business metrics, insights and recommendations.

The project simulates a small retail analytics workflow: raw order data is loaded from CSV, processed through reusable Python functions, validated with automated tests and summarized into business-friendly recommendations.

## Project Overview

This project demonstrates how Python can be used to support retail decision-making through:

- order value calculations
- discount and VAT calculations
- profit and profit margin analysis
- order classification
- business KPI summaries
- rule-based assistant insights
- automated unit testing with pytest

The assistant does not use external APIs or private data. It is built as a transparent, testable Python project suitable for a junior Data Analyst / Python / AI portfolio.

## Key Features

- Load retail orders from CSV using pandas
- Calculate initial order value, discount value, VAT, final customer price and profit
- Classify orders as small, medium or large
- Classify profit status as profit, loss or break-even
- Generate business-level KPIs such as total revenue, total profit and profit margin
- Identify largest, smallest, most profitable and least profitable orders
- Generate simple business insights and recommendations
- Validate the business logic with automated pytest tests

## Technologies Used

- Python
- pandas
- pytest
- Git and GitHub

## Project Structure

```text
ai-retail-assistant/
  data/
    orders.csv
  methods/
    assistant.py
    order_processing.py
    sales.py
  tests/
    test_assistant.py
    test_order_processing.py
    test_sales.py
  main.py
  pyproject.toml
  README.md
  PROJECT_LOG.md
```

## Sample Data

The project uses fictional retail order data:

```text
order_id,quantity,unit_price,unit_cost,discount_percent,vat_percent
ORD001,3,200,150,10,21
ORD002,5,120,90,0,21
ORD003,2,100,120,10,21
```

## How To Run

Create and activate a virtual environment, then install the project dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -e ".[dev]"
```

Run the demo:

```bash
python main.py
```

Run the tests:

```bash
python -m pytest -q
```

## Example Output

```text
AI Retail Assistant
===================

Business insights:
- Total revenue before VAT is 1,320.00, with total customer payments of 1,597.20.
- Total profit is 180.00, with a profit margin of 13.64%.
- 66.67% of orders are profitable, while 33.33% generate a loss.

Recommendations:
- Review loss-making orders and compare unit cost, discount level and final price.
- Profit margin is below 15%, so pricing, discounts and product costs should be reviewed.
```

## Testing

The project includes automated tests for:

- sales calculations
- discount and VAT logic
- order classification
- CSV loading and order processing
- business KPI calculations
- assistant insight generation

Current test status:

```text
153 passed
```

## Portfolio Value

This project demonstrates:

- Python fundamentals
- clean business logic
- data analysis thinking
- retail KPI interpretation
- automated testing
- Git/GitHub workflow
- ability to turn data into actionable recommendations

## Author

Cecilia Ionita
