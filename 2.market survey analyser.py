# market survey analyser
#skills: for loop, dicts, counting

preferences = ["coffee", "tea", "coffee", "soda"]
counts = {}
for item in preferences:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

total = len(preferences)

print("\n--- Market Share Summary ---")

for product in counts:
    percentage = (counts[product] / total) * 100
    print(f"{product}: {percentage:.0f}%")