# modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

print()  # blankline
#==============================================================================#
# appending elements to a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

print()  # blankline
#==============================================================================#
# starting with an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

print()  # blankline
#==============================================================================#
# inserting elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)

print()  # blankline
#==============================================================================#
# removing elements from a list using their index
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)
# delete the second item in the list
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

print()  # blankline
#==============================================================================#
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(f"The popped motorcycle, {popped_motorcycle.title()}, can be used and inserted.")

# popping items from any position in the list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

print()  # blankline
#==============================================================================#
# removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

print()  #blankline
# remove an item by value and print a reason
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
