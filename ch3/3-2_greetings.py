names = ['jorge', 'jennifer',  'alexander', 'adam', 'juan']

# print a message for each name in the list
print(f"Hello, {names[0].title()}, I hope you are enjoying VS Code and Python!")
print(f"Hello, {names[1].title()}, I hope you are enjoying VS Code and Python!")
print(f"Hello, {names[2].title()}, I hope you are enjoying VS Code and Python!")
print(f"Hello, {names[3].title()}, I hope you are enjoying VS Code and Python!")
print(f"Hello, {names[-1].title()}, I hope you are enjoying VS Code and Python!")

print() # blank line

# you can also use a variable to store the message
msg = f"Hello, {names[0].title()}, I hope you are enjoying VS Code and Python!"
print(msg)

msg = f"Hello, {names[-2].title()}, I hope you are enjoying VS Code and Python!"
print(msg)

