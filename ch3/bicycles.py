# square brackets indicate a list, individual elements are separated by commas
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

### Accessing Elements in a List
# access the first element in the list
print(bicycles[0])

# you can use a string method to capitalize the first letter of the first element
print(bicycles[0].title())

# index positions start at 0, not 1
print(bicycles[1])
print(bicycles[3])

# to access the last element in the list, use -1
print(bicycles[-1])
# this is the same as bicycles[3]

# to access the second to last element in the list, use -2
print(bicycles[-2])

### Using Individual Values from a List
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
