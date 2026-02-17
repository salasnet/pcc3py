# 3.6_MoreGuests_zu.py

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

print() # blank line
# print the invitations again
print(f"Mr. {guests[0].title()}, {dinnermsg}")
print(f"Mr. {guests[1].title()}, {dinnermsg}")
print(f"Mr. {guests[2].title()}, {dinnermsg}")
print(f"Mr. {guests[3].title()}, {dinnermsg}")
print(f"Mr. {guests[4].title()}, {dinnermsg}")
print(f"Mr. {guests[5].title()}, {dinnermsg}")
