'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''
*************************
print("This program will calculate the cost of your trip.")
miles = float(input("How many miles will you drive?"))
mpg = float(input("How many miles do you get per gallon?"))
price_gallon = float(input("How many USD does one gallon of fuel cost?"))
gallons_needed = miles / mpg
total_price = gallons_needed * price_gallon
print("Your trip will cost", total_price, "USD.")
*************************
