# Create a list and then use very function in chapter 3 on the list
friends = ['tea', 'kat', 'poke', 'katie', 'purse']

#==============================================================================#
# print different items of the list with .title, .upper, and .lower
print(friends)
print(friends[0])
print(friends[0].title())
print(friends[3].title())
print(friends[1].upper())
print(friends[2].lower())
print(friends[-1])

################################################################################
# create an f string variable  featuring an item from the list
message = f"My closest friend is {friends[1].title()}."
print(message)

print()  # blankline
#==============================================================================#
# modify and add items to a list using append and insert
friends[0] = 'cran'
print(friends)
friends = ['tea', 'kat', 'poke', 'katie', 'purse']
print(friends)
friends.append('cran')
print(friends)
friends = ['tea', 'kat', 'poke', 'katie', 'purse']
friends.insert(0, 'cran')
print(friends)

print()  # blankline
#==============================================================================#
# remove elements from the list with the pop method and then print messages using the popped items
del friends[0]
print(friends)
popped_friend = friends.pop()
print(friends)
print(popped_friend)
print(f"One of the silliest friends I know is {popped_friend.title()}.")
my_name = friends.pop(0)
print(f"My name is {my_name.title()}, maybe we can be friends too?")

print()  # blankline
#==============================================================================#
# remove elements from the list using the remove function to remove by value
friends = ['tea', 'kat', 'poke', 'katie', 'purse']
print(friends)
not_a_friend = 'tea'
friends.remove(not_a_friend)
print(friends)
print(f"\n{not_a_friend.title()} is technically not a friend, because that's me!")

print()  # blankline
#==============================================================================#
# Sort a list both permanently and temporarily with the sort() and sorted() functions
friends = ['tea', 'kat', 'poke', 'katie', 'purse']
friends.sort()
print("I changed the list of me and my friends to be sorted alphabetically!")
print(friends)
print(f"\nNow I changed it to be in reversed alphabetical order.")
friends.sort(reverse=True)
print(friends)
print(f"\nI can still show you the list in alphabetical order though!")
print(sorted(friends))
print(f"\nOne more time in reversed alphabetical~! ^w^")
print(sorted(friends, reverse=True))

print()  # blankline
#==============================================================================#
# Reprint the original list, and then reverse the list nonalphabetically
friends = ['tea', 'kat', 'poke', 'katie', 'purse']
print(friends)
friends.reverse()
print("Here are me and my friends but flipped around, UNO reverse!")
print(friends)

print()  # blankline
#==============================================================================#
# Find the length of the list using the len() function
friends = ['tea', 'kat', 'poke', 'katie', 'purse']
print(len(friends))
print(f"The amount of friends on my list, including myself, is {len(friends)}.")