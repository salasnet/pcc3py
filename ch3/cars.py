# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# You can also sort in reverse-alphabetical list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#==============================================================================#
print("---------") # seperator

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#==============================================================================#
print("---------") # seperator

# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

#==============================================================================#
print("---------") # seperator

# Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
