# DATA 4000 – Python with AI Assignment 3

This repository contains solutions for **Assignment 3** of the course **DATA 4000: Python with AI**.  
The programs demonstrate core Python concepts including loops, dictionaries, nested loops, functions, conditionals, and business-style calculations.

All code is written in **Python 3** and intended to be run from the command line using **Visual Studio Code**.

---

## 1: Retail Checkout Simulation  
File: `1_Retail Checkout Simulation.py`

Prompts the user to enter item prices until `0` is entered. Stores prices in a list and prints the number of items, total amount, and average item cost.

Assumptions:
- Prices are numeric inputs.
- Entering `0` ends the input process.
- Negative prices are not valid.

---

## 2: Market Survey Analyser  
File: `2.market survey analyser.py`

Analyzes a list of customer product preferences. Counts selections using a dictionary and prints a percentage-based market share summary.

Assumptions:
- Survey responses are provided in a predefined list.
- Percentages are calculated from total responses.

---

## 3: Expense Report Categorizer  
File: `3.Expense Report Categorizer.py`

Uses a dictionary of expense categories (each containing a list of values). Calculates category totals and a grand total using nested loops and prints a summary report.

Assumptions:
- Expense values are numeric.
- Data is stored in a dictionary of lists.

---

## 4: Sales Commission Calculator  
File: `4.Sales commission calculator.py`

Calculates employee commissions from sales data using a function, then prints a ranked leaderboard based on commission earned.

Assumptions:
- Sales data is stored in a dictionary.
- Commission rate follows assignment instructions.

---

## 5: Stock Portfolio Tracker  
File: `5.stock portfolio tracker.py`

Calculates the value of each stock position and the total portfolio value using nested dictionaries and loops.

Assumptions:
- Shares and prices are numeric.
- Portfolio data is predefined.

---

## 6: Bank Loan Repayment Simulator  
File: `6.Bank loan repayment simulator.py`

Simulates month-by-month repayment of a loan using a while loop. Calculates how many months it takes to pay off the loan based on loan amount, interest rate, and monthly payment.

Assumptions:
- Inputs are numeric.
- Interest is applied monthly based on an annual rate.

---

## 7: Simple Supply Chain Tracker  
File: `7.simple supply chain tracker.py`

Models multiple warehouses and their inventories. Aggregates total inventory across warehouses using nested loops.

Assumptions:
- Warehouses are stored as a list of dictionaries.
- Inventory quantities are numeric.

---

## 8: Customer Loyalty Tiers  
File: `8.customer loyalty tiers.py`

Classifies customers into tiers (e.g., Bronze/Silver/Gold) based on spending and prints a tier summary.

Assumptions:
- Customer spending data is stored in a dictionary.
- Tier thresholds follow assignment instructions.

---

## 9: Business Growht Projection  
File: `9.business Growht projection.py`

Projects revenue growth over time using compound growth calculations and prints a year-by-year projection.

Assumptions:
- Growth rate is entered as a percentage.
- Revenue compounds each year.

---

## 10: Startup Pitch Deck Visualizer  
File: `10.Startup pitch deck visualizer.py`

Creates an ASCII-style visualization (using `#`) to display growth or performance trends in the terminal.

Assumptions:
- Values are scaled to fit terminal output.
- Visualization represents relative growth.

---

## ▶️ How to Run
1. Open this repository in **Visual Studio Code**
2. Open a terminal
3. Run a program using:

```bash
python "1_Retail Checkout Simulation.py"
```

Tip: Because many filenames include spaces, run them using quotes (as shown above).
