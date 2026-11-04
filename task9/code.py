# Multi-Day Water Tank Simulation

capacity = float(input("Enter tank capacity: "))
level = float(input("Enter initial water level: "))
threshold = float(input("Enter water level threshold: "))
days = int(input("Enter number of days: "))

overflow_count = 0
shortage_count = 0
first_interval = -1

for i in range(1, days + 1):

    print("\nDay", i)

    inflow = float(input("Enter water inflow: "))
    outflow = float(input("Enter water outflow: "))

    # Calculate water level
    level = level + inflow - outflow

    overflow = 0
    shortage = 0

    # Check overflow
    if level > capacity:
        overflow = level - capacity
        level = capacity
        overflow_count += 1

    # Check shortage
    if level < 0:
        shortage = abs(level)
        level = 0
        shortage_count += 1

    # Check threshold
    if level >= threshold and first_interval == -1:
        first_interval = i

    print("Current Water Level:", level)
    print("Overflow Quantity:", overflow)
    print("Shortage Quantity:", shortage)

# Final report
print("\n--- Water Tank Report ---")
print("Final Water Level:", level)
print("Overflow Occurrences:", overflow_count)
print("Shortage Occurrences:", shortage_count)

if first_interval != -1:
    print("First Threshold Reached: Day", first_interval)
else:
    print("Threshold Not Reached")

print("Simulation Completed")
