# Campus Event Seating and Entry Validation

rows = 3
seats = 4

seating = [[0 for j in range(seats)] for i in range(rows)]

registrations = ["101", "102", "103", "104",
                 "105", "106", "107", "108"]

# Generate seating assignments
index = 0

for i in range(rows):
    for j in range(seats):
        if index < len(registrations):
            seating[i][j] = registrations[index]
            index += 1

print("Seating Assignments:")
for row in seating:
    print(row)

# Ticket validation
entered = set()
valid = 0
invalid = 0
duplicate = 0

n = int(input("\nEnter number of ticket entries: "))

for i in range(n):
    ticket = input("Enter Registration ID: ")

    if ticket not in registrations:
        print("Invalid Ticket")
        invalid += 1

    elif ticket in entered:
        print("Duplicate Entry")
        duplicate += 1

    else:
        print("Entry Allowed")
        entered.add(ticket)
        valid += 1

# Capacity calculation
total_seats = rows * seats
occupied = len(registrations)
available = total_seats - occupied

print("\n--- Event Report ---")
print("Valid Entries:", valid)
print("Invalid Tickets:", invalid)
print("Duplicate Entries:", duplicate)
print("Total Seating Capacity:", total_seats)
print("Occupied Seats:", occupied)
print("Available Seats:", available)
