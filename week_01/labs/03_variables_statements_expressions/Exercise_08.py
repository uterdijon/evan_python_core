'''
Celsius to Fahrenheit:

Write the necessary code to read a degree in Celsius from the console
then convert it to fahrenheit and print it to the console.

    F = C * 1.8 + 32

Output should read like - "27.4 degrees celsius = 81.32 degrees fahrenheit"

NOTE: if you get an error, look up what input() returns!

'''
***************************
temp_cel = int(input("This program converts temperature from Celsius to Farenheit. What is the temperature in Celsius?"))
temp_far = temp_cel * 1.8 + 32
print(temp_cel," degrees Celsius = ", temp_far, "degrees Farenheit.")
***************************
