def sumdigit(n):
    if n==0:
        return 0
    else:
        return (n%10)+sumdigit(n//10)
num=int(input("Enter n:"))
print("Sum of digit:",sumdigit(num))
[25bcs147@mepcolinux ex4]$cat ex4r.py
# Online Shopping Cart Billing System

# Each item is represented as a tuple: (item_name, quantity, price_per_unit)
cart = [
    ("Laptop", 1, 45000),
    ("Mouse", 2, 500),
    ("Keyboard", 1, 1500),
    ("Headphones", 1, 2000)
]

# Function to calculate subtotal for each item
def calculate_subtotal(cart):
    subtotals = []
    for item in cart:
        name, qty, price = item
        cost = qty * price
        subtotals.append((name, qty, price, cost))
    return subtotals

# Function to calculate total, discount, GST
def calculate_total(subtotals):
    subtotal_amount = sum(item[3] for item in subtotals)

    # Discount rule
    if subtotal_amount > 3000:
        discount = 0.10 * subtotal_amount
    else:
        discount = 0

    # GST 5%
    gst = 0.05 * (subtotal_amount - discount)

    total_amount = subtotal_amount - discount + gst
    return subtotal_amount, discount, gst, total_amount

# Display bill
def display_bill(cart):
    subtotals = calculate_subtotal(cart)
    subtotal_amount, discount, gst, total_amount = calculate_total(subtotals)

    print("------ BILL DETAILS ------")
    for item in subtotals:
        name, qty, price, cost = item
        print(f"{name} (x{qty}) @ Rs.{price}/unit = Rs.{cost}")

    print("\n------ SUMMARY ------")
    print(f"Subtotal: Rs.{subtotal_amount:.2f}")
    print(f"Discount: Rs.{discount:.2f}")
    print(f"GST (5%): Rs.{gst:.2f}")
    print(f"Total Amount: Rs.{total_amount:.2f}")

# Run the program
display_bill(cart)
