def is_even(N: int):
    return N%2 == 0

def calculator(a: int, b: int, operation: str):
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    if operation == "/":
        if b == 0:
            print("You cannot divide by 0!")
            return None
        else:
            return a / b        
        
def find_max(nums):
    ans = -1e18
    for num in nums:
        if num > ans:
            ans = num
    return ans