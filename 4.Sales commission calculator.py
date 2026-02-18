#Sales commission calculator
#skills: for loop, functions

sales = {
    "Alice": 5000,
    "Bob": 7000,
    "Carol": 3000
}

def calculate_commission(sales_amount):
    return sales_amount * 0.10

commissions = {}
for employee in sales:
    commissions[employee] = calculate_commission(sales[employee])

sorted_commissions = (sorted(commissions.items(), key=lambda item: item[1], reverse=True))

print("\n--- Commission Leaderboard ---")
for name, commission in sorted_commissions:
    print(f"{name}: ${commission:.2f}")