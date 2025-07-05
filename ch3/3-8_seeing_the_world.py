# 3.8_SeeingTheWorld_zu.py

places = ['sydney', 'tokyo', 'budapest', 'moscow', 'london']

print("Original order:")
print(places)

print("\nAlphabetical:")
print(sorted(places))
print("\nOriginal order:")
print(places)

print("\nReverse alphabetical:")
print(sorted(places, reverse=True))
print("\nOriginal order:")
print(places)

print("\nReversed:")
places.reverse()
print(places)

print("\nOriginal order:")
places.reverse()
print(places)

print("\nAlphabetical Permanent:")
places.sort()
print(places)

print("\nReverse alphabetical Permanent:")
places.sort(reverse=True)
print(places)