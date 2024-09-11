print("What year is it?")
current_year = input()

print("What is the first birth year?")
birth_year1 = input()

print("What is the second birth year?")
birth_year2 = input()

print("What is the third birth year?")
birth_year3 = input()

age1 = str(int(current_year)-int(birth_year1))
age2 = str(int(current_year)-int(birth_year2))
age3 = str(int(current_year)-int(birth_year3))

print("The input years were: " + birth_year1 + ", " + birth_year2 + " and " + birth_year3)
print("The probable ages are: " + age1 + ", " + age2 + " and " + age3)

average_age = str(int((int(age1) + int(age2) + int(age3)) / 3))
print("The average age is " + average_age)