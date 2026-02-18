#customer loyalty tiers
#skills: conditionals, dicts, loops

customers = {
    "Alice": 800,
    "Bob": 1200,
    "Carol": 6000,
    "David": 4500
}

tiers = {
    "Bronze": 0,
    "Silver": 0,
    "Gold": 0
}

for customer in customers:
    amount = customers[customer]

if amount < 1000:
        tiers["Bronze"] += 1
elif amount < 5000:
        tiers["Silver"] += 1
else:
        tiers["Gold"] += 1

print("\n--- Customer Loyalty Tiers summary ---")

for tier in tiers:
    print(f"{tier}: {tiers[tier]} customers")
