print("Type 5 different integers:")
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

arr = []
arr.append(num1)
if num2 not in arr:
    arr.append(num2)
if num3 not in arr:
    arr.append(num3)
if num4 not in arr:
    arr.append(num4)
if num5 not in arr:
    arr.append(num5)

print("Length of the list is: " + str(len(arr)))
print("Last element is: " + str(arr[len(arr)-1]))