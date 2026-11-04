# Retail Billing with Multiple Discount Rules

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0

print("\n--- Product Details ---")

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity

    # Category-specific tax
    if category.lower() == "food":
        tax_rate = 5
    elif category.lower() == "clothing":
        tax_rate = 5
    elif category.lower() == "electronics":
        tax_rate = 18
    else:
        tax_rate = 12

    tax = amount * tax_rate / 100

    subtotal += amount
    total_tax += tax

    print("Product Amount:", amount)
    print("Tax:", tax)

# Discount calculation
if subtotal >= 5000:
    discount_rate = 20
elif subtotal >= 3000:
    discount_rate = 10
elif subtotal >= 1000:
    discount_rate = 5
else:
    discount_rate = 0

discount = subtotal * discount_rate / 100

# Maximum discount limit
if discount > 1000:
    discount = 1000

final_bill = subtotal + total_tax - discount

print("\n======= FINAL INVOICE =======")
print("Subtotal:", round(subtotal, 2))
print("Total Tax:", round(total_tax, 2))
print("Discount:", round(discount, 2))
print("Final Bill:", round(final_bill, 2))
print("=============================")
