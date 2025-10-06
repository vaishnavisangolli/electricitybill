# electricity_bill.py

# Program to calculate electricity bill

# Rate per unit
rate_per_unit = 75

# Get input from the user
units = int(input("Enter the number of units consumed: "))

# Calculate total bill
total_bill = units * rate_per_unit

# Display the bill
print(f"Units Consumed: {units}")
print(f"Total Bill: ₹{total_bill}")
