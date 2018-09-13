message = input("Enter a message: ")
number = int(input("Enter a number: "))
final_message = ""
for char in message:
    enumerated = ord(char)
    transformed = enumerated + number
    new_letter = chr(transformed)
    final_message += new_letter
print("Your encoded message is: ",final_message)


