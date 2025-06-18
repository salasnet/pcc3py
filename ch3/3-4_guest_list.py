# dinner list with three people
dinner_guests = ['beethoven', 'mozart', 'vivaldi']

msg = f"{dinner_guests[0].title()}, you are invited to dinner."
print(msg)
msg = f"{dinner_guests[1].title()}, you are invited to dinner."
print(msg)
msg = f"{dinner_guests[2].title()}, you are invited to dinner."
print(msg)

print() # blank line
# ---------------------------------------------------------
# solution 2
name = dinner_guests[0].title()
print(f"{name}, please come to dinner.")

name = dinner_guests[1].title()
print(f"{name}, please come to dinner.")

name = dinner_guests[2].title()
print(f"{name}, please come to dinner.")

print() # blank line
# ---------------------------------------------------------
# solution 3
print(f"{dinner_guests[0].title()}, dinner at my place. Be there.")
print(f"{dinner_guests[1].title()}, dinner at my place. Be there.")
print(f"{dinner_guests[2].title()}, dinner at my place. Be there.")