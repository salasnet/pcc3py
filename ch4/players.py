# players.py

# Working with Part of a List
# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # first three players only
print(players[1:4])  # second to fourth only
print(players[:4])   # omit first argument, starts at beginning
print(players[2:])   # omit last argument, goes to end
# negative index returns element distance from end
print(players[-3:])  # last three of the list
# including third argument tells it how many items to skip between items
print(players[0:5:2])
print(players[0::2]) # last argument ommited to go to the end of the list

print() # blank line
#==============================================================================#
# Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())