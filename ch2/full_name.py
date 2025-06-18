first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(full_name)

# create a full message using an f-string
print(f"Hello, {full_name.title()}!")

# this time, assign the message to a variable first, then print it
message = f"Hello, {full_name.title()}!"
print(message)