# 4.8 Cubes

cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
print(cubes)

# omit intermediate variable
cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

for cube in cubes:
    print(cube)