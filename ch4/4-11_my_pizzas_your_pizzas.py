# 4.11 My Pizzas Your Pizzas
pizzas = ['sausage', 'pepperoni', 'supreme']

# create a copy of the list using a slice
friend_pizzas = pizzas[:]

# add a new pizza to the original list
pizzas.append('mushroom')
# add a new pizza to the friends list
friend_pizzas.append('veggie')

# Print my favorite pizzas
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print()

# Print my friends favorite pizzas
print("My friends favorite pizzas are:")
for friendpizza in friend_pizzas:
    print(f"- {friendpizza.title()}")
