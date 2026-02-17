# Retail Checkout Simulation
# skills: while loops, input validation, lists

prices = []

while True:
    price = float(input("Enter item price (0 to finish): "))

    if price == 0:
        break

    if price < 0:
        print("Invalid price. Try again.")
        continue

    prices.append(price)

count = len(prices)
total = sum(prices)

if count == 0:
    average = 0
else:
    average = total / count

print("\n--- Checkout Summary ---")
print(f"Items bought: {count}")
print(f"Total amount: ${total:.2f}")
print(f"Average item: ${average:.2f}")

