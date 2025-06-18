# dinner list with three people
dinner_guests = ['beethoven', 'mozart', 'vivaldi']
# print the invitations
print(f"{dinner_guests[0].title()}, dinner invitation to myplace.")
print(f"{dinner_guests[1].title()}, dinner invitation to myplace.")
print(f"{dinner_guests[2].title()}, dinner invitation to myplace.")

# guest who can't make it
print(f"\n{dinner_guests[0].title()} just messaged that he can't make it.")

# replace the guest who can't make it
dinner_guests[0] = 'chopin'
print("\nHere is the new guest list:")
# print the invitations again
print(f"{dinner_guests[0].title()}, dinner invitation to myplace.")
print(f"{dinner_guests[1].title()}, dinner invitation to myplace.")
print(f"{dinner_guests[2].title()}, dinner invitation to myplace.")
