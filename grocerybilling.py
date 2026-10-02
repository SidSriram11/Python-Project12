# ================================
# GROCERY BILLING QUEUE
# ================================

print("=== Grocery Billing Queue ===\n")

low_price_items = 0
medium_price_items = 0
high_price_items = 0
customers_served = 0
total_sales = 0
billing = True

while billing:
    customer_name = input("Enter customer's name: ")
    item_count = int(input(f"How many items is {customer_name} buying? "))

    if item_count <= 0:
        print("Invalid number of items. Moving to next prompt.\n")
        continue

    customer_total = 0
    item_number = 1
    
    while item_number <= item_count:
        print(f"\n--- Item {item_number} of {item_count} ---")
        item_name = input("Enter item name: ")
        price = int(input("Enter unit price: "))
        quantity = int(input("Enter quantity: "))

        if price <= 0 or quantity <= 0:
            print("Price and quantity must be greater than zero. Please re-enter this item.")
            continue
            
        item_total = price * quantity
        print(f"{item_name}: {quantity} x {price} = {item_total}")
        
        customer_total += item_total
        
        if price < 50:
            low_price_items += quantity
        elif 50 <= price <= 100:
            medium_price_items += quantity
        else:
            high_price_items += quantity
            
        item_number += 1

    customers_served += 1
    total_sales += customer_total
    
    print(f"\nTotal for {customer_name}: {customer_total}\n")
    
    next_customer = input("Next customer? (yes/no): ").strip().lower()
    print() 
    if next_customer != "yes":
        billing = False


print("=== End of Day Report ===")
print("Item Distribution Chart:")

bands = [
    ("Low Price (<50)   ", low_price_items),
    ("Medium Price (50-100)", medium_price_items),
    ("High Price (>100)  ", high_price_items)
]

for label, count in bands:
    print(f"{label}: ", end="")
    for _ in range(count):
        print("*", end="")
    print()

print(f"\nTotal Customers Served: {customers_served}")
print(f"Total Sales: {total_sales}")
