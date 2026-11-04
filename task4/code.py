# Manufacturing Cost and Profitability Analysis

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    quantity = int(input("Enter production quantity: "))

    material = float(input("Enter material cost per unit: "))
    labour = float(input("Enter labour cost per unit: "))
    wastage = float(input("Enter wastage percentage: "))
    machine = float(input("Enter machine cost per unit: "))
    selling = float(input("Enter selling price per unit: "))

    target = float(input("Enter profit target percentage: "))

    # Cost calculations
    material_cost = material * quantity
    labour_cost = labour * quantity
    machine_cost = machine * quantity

    wastage_cost = material_cost * wastage / 100

    total_cost = (material_cost + labour_cost +
                  machine_cost + wastage_cost)

    revenue = selling * quantity

    profit = revenue - total_cost

    if total_cost > 0:
        profit_percentage = (profit / total_cost) * 100
    else:
        profit_percentage = 0

    print("\n--- Production Report ---")
    print("Product Name:", name)
    print("Material Cost:", material_cost)
    print("Labour Cost:", labour_cost)
    print("Wastage Cost:", wastage_cost)
    print("Machine Cost:", machine_cost)
    print("Total Manufacturing Cost:", total_cost)
    print("Total Revenue:", revenue)
    print("Profit:", profit)
    print("Profit Percentage:", round(profit_percentage, 2), "%")

    if profit_percentage >= target:
        print("Result: Profit Target Achieved")
    else:
        print("Result: Profit Target Not Achieved")
