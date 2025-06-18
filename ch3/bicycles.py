# square brackets indicate a list, individual elements are separated by commas
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# access the first element in the list
print(bicycles[0])

# use a string method to capitalize the first letter of the first element
print(bicycles[0].title())

# the index starts at 0, not 1
print(bicycles[1])
print(bicycles[3])

# to access the last element in the list, use -1
print(bicycles[-1])
# this is the same as bicycles[3]

# to access the second to last element in the list, use -2
print(bicycles[-2])

# use individual values from a list
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
