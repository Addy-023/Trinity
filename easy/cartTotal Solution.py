# Shopping Cart Total
# Write a program that calculates the total price of a product based on the product selected and the quantity entered by the user. The program should support the 
# four available products and display the total amount that needs to be paid



headPhone = 999; #bug-remove ; string to integer conversion
smartWatch = 1599; #bug-remove ; string to integer conversion
ps5= 1299; #bug-remove ; string to integer conversion
iPad = 599; #bug-remove ; string to integer conversion


productName = input("Enter Product Name: "); #bug-remove ;


quantity = int(input("Enter the Quantity of the Product: ")); #bug-remove ; added int conversion to ensure quantity is an integer


if productName == "headPhone":
    totalPrice = headPhone * quantity; #bug-remove ;

elif productName == "smartWatch":
    totalPrice = smartWatch * quantity; #bug-remove ;

elif productName == "ps5":
    totalPrice = ps5 * quantity; #bug-remove ;

elif productName == "iPad":
    totalPrice = iPad * quantity; #bug-remove ;
else:
    totalPrice = 0; # added else case to handle invalid product names
    print("Invalid Product Name. Please select from headPhone, smartWatch, ps5, or iPad.") 

print(f"Total Amount To Be Paid: {totalPrice}") #bug-remove;