# Railway Fare and Reservation Calculator

n = int(input("Enter number of passengers: "))

total_collection = 0

for i in range(n):
    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = int(input("Enter journey distance: "))

    print("1. Sleeper")
    print("2. AC")
    print("3. General")

    choice = int(input("Select travel class: "))

    # Distance slab fare
    if distance <= 100:
        fare = distance * 1
    elif distance <= 500:
        fare = distance * 1.5
    else:
        fare = distance * 2

    # Travel class charges
    if choice == 1:
        fare = fare * 1.5
    elif choice == 2:
        fare = fare * 2.5
    elif choice == 3:
        fare = fare * 1
    else:
        print("Invalid class")
        continue

    # Age-based concession
    if age >= 60:
        fare = fare * 0.8
    elif age <= 12:
        fare = fare * 0.5

    reservation_fee = 50
    total_fare = fare + reservation_fee

    print("Ticket Fare:", round(total_fare, 2))

    cancel = input("Cancel ticket? (yes/no): ")

    if cancel.lower() == "yes":
        penalty = total_fare * 0.20
        refund = total_fare - penalty
        print("Cancellation Penalty:", round(penalty, 2))
        print("Refund Amount:", round(refund, 2))
        total_collection += penalty
    else:
        print("Final Fare:", round(total_fare, 2))
        total_collection += total_fare

print("\n--- Railway Report ---")
print("Total Railway Collection:", round(total_collection, 2))
