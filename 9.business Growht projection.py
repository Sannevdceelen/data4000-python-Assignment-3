#business Growht projection
#skills: for loops, math

initial_revenue = float(input("Enter the initial revenue: "))
growth_rate_percentage = float(input("Enter the annual growth rate (as a percentage): "))

growth_rate = growth_rate_percentage / 100

revenue = initial_revenue

print("\n--- 10-year revenue projection ---")
print("Year | Revenue")
print("-------------------")

for year in range(1, 11):
    revenue = revenue * (1 + growth_rate)
    print(f"{year:>4} | ${revenue:,.2f}")
    