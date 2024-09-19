# AUTHOR: Trevor Conger UNWSP 
# DATE: 9/19/24 
# TITLE: Weight > or < 

# Weight    	Price Per Pound
# 2 pounds or less   	$1.50
# Over 2 pounds but not more than 6 pounds  	$3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	$4.75
# Write a program which calculates the shipping charge and displays the total.


# This function takes in a float ( weight ) to calculate the shipping cost
def weight_conversion(weight):
    shippingCost = 0.0
    if weight <= 2: 
        shippingCost = weight * 1.5
    elif 2 < weight <= 6: 
        shippingCost = weight * 3.00
    elif 6 < weight <= 10: 
        shippingCost = weight * 4.00
    elif weight > 10: 
        shippingCost = weight * 4.75
    return shippingCost

#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))