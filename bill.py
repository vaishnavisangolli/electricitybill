# electricity_bill.py

# Electricity Bill Calculator with Discount Feature

# Rate per unit
rate_per_unit = 75

# Get input from user
units = int(input("Enter the number of units consumed: "))

# Calculate total bill
total_bill = units * rate_per_unit

# Check if discount applies
discount = 0
if total_bill > 1000:
    discount = total_bill * 0.10  # 10% discount

# Final bill after discount
final_bill = total_bill - discount

# Display results
print(f"Units Consumed: {units}")
print(f"Total Bill: ₹{total_bill}")
if discount > 0:
    print(f"Discount Applied: ₹{discount}")
print(f"Final Bill: ₹{final_bill}")