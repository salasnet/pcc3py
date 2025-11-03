# Chapter 4 Multiplication Table Exercise (bonus)

# Write code that will print a multiplication table from 1 to 10 for the numbers 2-9.
# Your output should look like this:

# Multiplication Table for 2:
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20
# 
# Multiplication Table for 3:
# 3 x 1 = 2
# 3 x 2 = 4
# etc.

# You should have in your code:
# 
# A print statement for the header of the table with an embedded variable.
# A variable for the number being multiplied.
# A range for the multipliers created in a loop.
# A variable with the calculation for the multiplication table.
# A looped print statement for the multiplication table itself.
# An empty line to separate each table.
################################################################################
# Multiplication Tables

# this example works but does not include the variable with the calculation
# the calculation is written out in the print statement
number = 2
print(f"Multiplication Table for {number}:")
for multiplier in range(1,10):
    print(f"{number} x {multiplier} = {number * multiplier}")

# Create a multiplication table with a variable called 'result' for the calculation
number = 2
print(f"Multiplication table for {number}:")
for multiplier in range(1,11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")

print()

# now we copy and paste the working code and change the number variable for each table

number = 3
print(f"Multiplication Table for {number}:")
for multiplier in range(1,10):
    result = (number * multiplier)
    print(f"{number} x {multiplier} = {result}")

print()

number = 4
print(f"Multiplication Table for {number}:")
for multiplier in range(1,10):
    result = (number * multiplier)
    print(f"{number} x {multiplier} = {result}")

print()

number = 5
print(f"Multiplication Table for {number}:")
for multiplier in range(1,10):
    result = (number * multiplier)
    print(f"{number} x {multiplier} = {result}")

print()

number = 6
print(f"Multiplication Table for {number}:")
for multiplier in range(1,10):
    result = (number * multiplier)
    print(f"{number} x {multiplier} = {result}")

print()

number = 7
print(f"Multiplication Table for {number}:")
for multiplier in range(1,10):
    result = (number * multiplier)
    print(f"{number} x {multiplier} = {result}")

print()

number = 8
print(f"Multiplication Table for {number}:")
for multiplier in range(1,10):
    result = (number * multiplier)
    print(f"{number} x {multiplier} = {result}")

print()

number = 9
print(f"Multiplication Table for {number}:")
for multiplier in range(1,10):
    result = (number * multiplier)
    print(f"{number} x {multiplier} = {result}")
    

################################################################################

# Can you streamline the code used for printing multiplication tables so that you only need two loops and seven lines of code (or even six)?
# 
# You will need a list with the numbers you will be multiplying, created with a range.
# 
# You will need a loop within a loop (nested loop) to print each multiplication table over and over again and its calculations.
# 
# You should have in your code:
# 
# A list with the range of numbers you will be multiplying.
# A for loop that goes through each number in your range of numbers you will be multiplying.
# A print statement inside the loop for the header of the table with an embedded variable.
# A loop with a range for the multipliers.
# A variable with the calculation for the multiplication table.
# A looped print statement for the multiplication table itself.
# An empty line to separate each table.

# 2 Multiplication Tables using a nested loop

print() # blank line
print("#################### Using a Nested Loop ###################")
print() # blank line

# Create a list of numbers 2-9
numbers = list(range(2, 10))

for num in numbers:
    print(f"Multiplication table for {num}:")
    for multiplier in range(1, 11):  # Loop 10 times for each number
        result = num * multiplier
        print(f"{num} x {multiplier} = {result}")
# Add an empty line after each table
    print()
