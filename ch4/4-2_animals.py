# 4.2 Animals
animals = ['cat', 'lion', 'panther']
for animal in animals:
    print(animal)

print("-----")
#==============================================================================#
# print a statement about each animal using f-strings
animals = ['cat', 'lion', 'panther']
for animal in animals:
    print(f"A {animal} has a long tail.")
    
print("-----")
#==============================================================================#
# add a line outside the loop to finish
animals = ['cat', 'lion', 'panther']
for animal in animals:
    print(f"A {animal} has a long tail.")
print(f"\nAll cats, big and small, have long tails.")