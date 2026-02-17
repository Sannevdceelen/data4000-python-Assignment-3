#Expense Report Categorizer
#Skills: nested loops, dicts

expenses = {
    "Travel": [500, 200],
    "Meals": [40, 60, 30],
    "Supplies": [100]
}

grand_total = 0

print("\n--- Expense summary Report ---")

for category in expenses:
    category_total = 0
    for amount in expenses[category]:
        category_total += amount
    print(f"{category}: ${category_total}")
    grand_total += category_total

print("-----------------------------")
print(f"Grand Total: ${grand_total}")   