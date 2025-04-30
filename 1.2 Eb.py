# Input customer number and units consumed
cno = int(input("Enter the customer number: ")) 
units = int(input("Enter the number of units consumed: ")) 

# Initialize variables
chrg = 0
surcharge = 0
total_amt = 0

# Calculate charge based on unit consumption
if units <= 200: 
    chrg = 0.50 * units 
elif units <= 400: 
    chrg = (0.50 * 200) + (0.65 * (units - 200)) 
elif units <= 600: 
    chrg = (0.50 * 200) + (0.65 * 200) + (0.85 * (units - 400)) 
else: 
    chrg = (0.50 * 200) + (0.65 * 200) + (0.85 * 200) + (1.00 * (units - 600)) 

# Apply surcharge if bill exceeds Rs. 400
if chrg > 400: 
    surcharge = chrg * 15 / 100 
    total_amt = chrg + surcharge 
else:
    total_amt = chrg

# Ensure minimum bill is Rs. 100
if total_amt < 100: 
    total_amt = 100 

# Output the details
print("\nCustomer number:", cno) 
print("Units consumed:", units) 
print("Charge: Rs.", chrg) 
print("Surcharge amount: Rs.", surcharge) 
print("Total amount to be paid by customer: Rs.", total_amt)
