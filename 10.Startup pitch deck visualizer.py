#startup pitch deck visualizer
#skills: nested loops, string multiplication

initial_revenue = float(input("enter initial revenue:"))
growth_rate_percent = float(input("enter annual growth rate (in percentage):"))

growth_rate_percent = growth_rate_percent / 100
revenue = initial_revenue

print("\n--- Projected Revenue Chart ---")

for year in range(1, 6):
    revenue = revenue * (1 + growth_rate_percent)

    scaled_value = int(revenue / 10000)
    print(f"Year {year}: " + "#" * scaled_value)
    
          