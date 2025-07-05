# 4.13 Buffet

# tuple of five foods
menu_items = ('crab cakes', 'lobster roll', 'fish sandwich', 'patty melt', 'house salad')
for food in menu_items:
    print(food.title())

# try to change one
# basic_foods[0] = 'cakes'

print()

# tuple of new menu
menu_items = ('crab cakes', 'calamari', 'fish sandwich', 'chanquetes', 'house salad')
for food in menu_items:
    print(food.title())

print()


# FANCIER
# insert breaks so that the tuple line is not so long
# add Title formatting and a statement before the list
menu_items = (
    'crab cakes', 'lobster roll', 'fish sandwich',
    'patty melt', 'house salad'
    )
print("You may choose from the following menu items:")
for food in sorted(menu_items):
    print(f"- {food.title()}")

print()

menu_items = (
    'crab cakes', 'calamari', 'fish sandwich',
    'oysters', 'house salad'
    )
print("Our new menu items are:")
for food in sorted(menu_items):
    print(f"- {food.title()}")
