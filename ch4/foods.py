# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # copy the list using a slice with no arguments
#friend_foods = my_foods  # this doesnt' work, does not make a copy

# add unique items to each list to make them different
my_foods.append('canoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)