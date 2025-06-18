# Variables for the name and the message. The message has an embedded f-string variable
name = 'jennifer'
message = f"Hello {name.title()}, would you like to learn some Python today?"

print(message)

# you can also not use the second variable and put your string in the print function
print(f"Hello {name.title()}, would you like to learn some Python today?")