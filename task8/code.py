# Smart Parking Fee Management

from datetime import datetime

n = int(input("Enter number of vehicles: "))

total_collection = 0

for i in range(n):
    print("\nVehicle", i + 1)

    number = input("Enter vehicle number: ")
    category = input("Enter category (bike/car/bus): ")

    entry = input("Enter entry time (HH:MM): ")
    exit_time = input("Enter exit time (HH:MM): ")

    try:
        start = datetime.strptime(entry, "%H:%M")
        end = datetime.strptime(exit_time, "%H:%M")

        if start == end:
            print("Invalid parking duration")
            continue

        if end < start:
            end = end.replace(day=2)

        duration = (end - start).total_seconds() / 3600

        # Vehicle category rates
        if category.lower() == "bike":
            rate = 10
        elif category.lower() == "car":
            rate = 20
        elif category.lower() == "bus":
            rate = 40
        else:
            print("Invalid vehicle category")
            continue

        # Calculate parking fee
        hours = int(duration) + (duration % 1 > 0)

        fee = hours * rate

        # Daily maximum limit
        daily_limit = 200

        if fee > daily_limit:
            fee = daily_limit

        # Overnight parking charge
        penalty = 0

        if end.date() > start.date():
            penalty = 50

        total = fee + penalty
        total_collection += total

        print("\n--- Parking Bill ---")
        print("Vehicle Number:", number)
        print("Vehicle Category:", category)
        print("Parking Duration:", round(duration, 2), "hours")
        print("Parking Fee:", fee)
        print("Overnight Penalty:", penalty)
        print("Total Parking Fee:", total)

    except ValueError:
        print("Invalid time format! Use HH:MM.")

print("\n--- Parking Summary ---")
print("Total Vehicles:", n)
print("Total Collection:", total_collection)
