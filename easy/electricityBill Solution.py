# Electricity Bill Calculator
# Write a program that calculates the electricity bill based on units consumed using different rates for different slabs.

# 100 and below = 3
# 100-200 = 5
# 200-300 = 7
# 300 above = 10


# Taking Units Consumed as Input
units = float(input("Enter Units Consumed: "));   # added float conversion to ensure units is treated as a number for calculations


# Calculating Bill Based on Slabs
if units <= 100:  #changed from '==' to '<=' to include all values 100 and below
    totalBill = units * 3;

elif units <= 200: #changed from '==' to '<=' to include all values between 101 and 200, and added parentheses for correct order of operations
    totalBill = 100*3 + (units-100)*5; #wrong calculation, should be 100*3 + (units-100)*5

elif units <= 300: #changed from '==' to '<=' to include all values between 201 and 300, and added parentheses for correct order of operations
    totalBill = 100*3 + 100*5 + (units-200)*7;#wrong calculation, should be 100*3 + 100*5 + (units-200)*7

else:
    totalBill = 100*3 + 100*5 + 100*7 + (units-300)*10; #wrong calculation, should be 100*3 + 100*5 + 100*7 + (units-300)*10

# Displaying the Final Bill
print(f"Total Electricity Bill: {totalBill}")#removed semicolon at the end of the print statement