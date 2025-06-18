# Adding Whitespace
print("Python")
print("\tPython")

print()
print("Languages:\nPython\nC\nJavaScript")
print("\nLanguages:\n\tPython\n\tC\n\tJavaScript")

# Stripping Whitespace
favorite_language = 'python '
print(favorite_language.rstrip())
# this only removes it temporarily
# reassign the variable with the rstrip to make it permanent
favorite_language = favorite_language.rstrip()
print(favorite_language)

# rstrip(), lstrip(), strip()
favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

# Removing Prefixes
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))
print(nostarch_url.removesuffix('.com'))