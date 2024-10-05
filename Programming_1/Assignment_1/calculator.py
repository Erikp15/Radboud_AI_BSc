print("Choose one operation {sum, subtraction, multiplication, division}:")
operation = input()

print("Type the first number:")
number_1 = int(input())

print("Type the second number:")
number_2 = int(input())

if operation == "sum":
    print(number_1 + number_2)

if operation == "subtraction":
    print(number_1 - number_2)

if operation == "multiplication":
    print(number_1 * number_2)

if operation == "division":
    if number_2 == 0:
        print("Division by 0 is not possible!")
    if number_2 != 0:
        print(number_1 / number_2)