# 3.7_ShrinkingGuestList_zu.py

# Code from 3.6
# guest list
guests = ['beethoven', 'mozart', 'vivaldi']

# dinner message
dinnermsg = "you are cordially invited to dinner."

# print each guest a dinner message
print(f"Mr. {guests[0].title()}, {dinnermsg}")
print(f"Mr. {guests[1].title()}, {dinnermsg}")
print(f"Mr. {guests[2].title()}, {dinnermsg}")

print()
# print the person who cannot make it, removed from end of list
print(f"Mr. {guests[-1].title()} cannot make it to dinner")

# remove the last person from the list and replace them
guests[-1] = 'bach'

print()

# print the invitations again
print(f"Mr. {guests[0].title()}, {dinnermsg}")
print(f"Mr. {guests[1].title()}, {dinnermsg}")
print(f"Mr. {guests[2].title()}, {dinnermsg}")

print()  # blankline
#==============================================================================#
# inform the guests that we now have a bigger table
print("Good news! We have found a bigger table for dinner and will be adding additional guests.")

# insert and append the new guests to our list
guests.insert(0, 'williams')
guests.insert(2, 'shostakovich')
guests.append('haydn')

# check to make sure our list is OK
# print(guests)
# print(len(guests))

print()
# print the invitations again
print(f"Mr. {guests[0].title()}, {dinnermsg}")
print(f"Mr. {guests[1].title()}, {dinnermsg}")
print(f"Mr. {guests[2].title()}, {dinnermsg}")
print(f"Mr. {guests[3].title()}, {dinnermsg}")
print(f"Mr. {guests[4].title()}, {dinnermsg}")
print(f"Mr. {guests[5].title()}, {dinnermsg}")

print()  # blankline
#==============================================================================#
# 3.7 New Code

print("Unfortunately, only two people will be able to attend dinner now.")

print()
noguest = guests.pop(0)
print(f"{noguest.title()}, you are no longer invited to dinner.")
noguest = guests.pop(0)
print(f"{noguest.title()}, you are no longer invited to dinner.")
noguest = guests.pop(0)
print(f"{noguest.title()}, you are no longer invited to dinner.")
noguest = guests.pop(0)
print(f"{noguest.title()}, you are no longer invited to dinner.")

# to check my list and how many are in it
# print(guests)
# print(len(guests))

# dinner message
dinnermsg2 = "you are still invited to dinner."

print()
# print the invitations again
print(f"Mr. {guests[0].title()}, {dinnermsg2}")
print(f"Mr. {guests[1].title()}, {dinnermsg2}")


# delete the last two guests
del guests[0]
del guests[0]

# empty list proof
print(guests)