# Tuples

dimensions = (200, 50)
# dimensions[0] = 250  # cannot change a tuple
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

print()
#==============================================================================#
# Writing Over a Tuple
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

# replace the tuple completely
dimensions = (400, 100)
print('\nNew dimensions:')
for dimension in dimensions:
    print(dimension)