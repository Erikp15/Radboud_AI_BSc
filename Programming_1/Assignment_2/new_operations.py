num1 = int(input("Input the first positive integer:"))
num2 = int(input("Input the second positive integer:"))

if num1 < num2:
    num3 = num1
    num1 = num2
    num2 = num3

print(num1//num2)
print(num1%num2)

if num2 < 5:
    print(num2**num1)