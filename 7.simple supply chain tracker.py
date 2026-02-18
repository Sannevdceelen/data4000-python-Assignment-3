#simple supply chain tracker
#skills: nested loops, lists of dicts

warehouses = [
    {"name": "Warehouse A", "inventory": {"Apples": 100, "Bananas": 150}},
    {"name": "Warehouse B", "inventory": {"Apples": 200, "Bananas": 100}}
]

total_inventory = {}
for warehouse in warehouses:
    inventory = warehouse["inventory"]
    for product in inventory:
        quantity = inventory[product]

        if product in total_inventory:
            total_inventory[product] += quantity
        else:
            total_inventory[product] = quantity

print("\n--- Total Inventory Across Supply Chain ---")

for product in total_inventory:
    print(f"{product}: {total_inventory[product]}")
    