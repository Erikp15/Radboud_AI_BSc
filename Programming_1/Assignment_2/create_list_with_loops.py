print("Type 5 different integers:")

arr = []
for i in range(5):
    num = int(input())
    if num not in arr:
        arr.append(num)

print("Length of the list is: " + str(len(arr)))
print("Last element is: " + str(arr[len(arr)-1]))