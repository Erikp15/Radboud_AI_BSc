print("Choose the operation:")
print("- sum [1]")
print("- subtraction [2]")
print("- multiplication [3]")
print("- division [4]")

operation = int(input())

print("What's the first number:")
num1 = int(input())

print("What's the second number:")
num2 = int(input())

print("the result is:")

if operation < 2 or operation > 4:
    print(num1 + num2)
elif operation == 2:
    print(num1 - num2)
elif operation == 3:
    print(num1 * num2)    
else:
    print(num1 / num2)