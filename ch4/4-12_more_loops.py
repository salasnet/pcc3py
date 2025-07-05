# 4.12 More Loops
# foods.py with for loops

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

# add the new foods
my_foods.append('canoli')
friends_foods.append('ice cream')

# print my foods in Title case using a loop
print("My favorite foods are:")
for myfood in my_foods:
    print(myfood.title())

print()

# print my friend foods in Title case using a loop and sorting alphabetically
print("My friends favorite foods are:")
for friendfood in sorted(friends_foods):
    print(friendfood.title())
