# Warehouse Inventory Reconciliation

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    opening = int(input("Enter opening stock: "))
    incoming = int(input("Enter incoming quantity: "))
    dispatched = int(input("Enter dispatched quantity: "))
    actual = int(input("Enter actual closing stock: "))
    minimum = int(input("Enter minimum stock level: "))

    # Calculate expected closing stock
    expected = opening + incoming - dispatched

    # Check stock discrepancy
    difference = actual - expected

    print("\n--- Inventory Report ---")
    print("Product Name:", name)
    print("Opening Stock:", opening)
    print("Incoming Stock:", incoming)
    print("Dispatched Stock:", dispatched)
    print("Expected Closing Stock:", expected)
    print("Actual Closing Stock:", actual)

    if difference == 0:
        print("Stock Status: No Discrepancy")
    elif difference > 0:
        print("Stock Status: Excess Stock")
        print("Extra Quantity:", difference)
    else:
        print("Stock Status: Stock Shortage")
        print("Missing Quantity:", abs(difference))

    # Replenishment calculation
    required = max(0, minimum - actual)

    print("Replenishment Required:", required)

print("\nInventory Reconciliation Completed")
