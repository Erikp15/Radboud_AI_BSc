print("Name 1:")
name_1 = input()

print("birth year 1:")
year_1 = int(input())

print("Name 2:")
name_2 = input()

print("birth year 2:")
year_2 = int(input())

print("Name 3:")
name_3 = input()

print("birth year 3:")
year_3 = int(input())

if year_1 < year_2 and year_1 < year_3:
    print(name_1)
elif year_2 < year_1 and year_2 < year_3:
    print(name_2)
else:
    print(name_3)
