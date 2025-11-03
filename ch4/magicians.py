# magicians.py

# Don't forget the colon!
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

print()

# Doing More Work Within a for Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Doing Something After a for Loop (remove the indent)
print("Thank you, everyone. That was a great magic show!")