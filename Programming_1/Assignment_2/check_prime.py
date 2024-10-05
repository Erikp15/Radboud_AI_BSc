def factors(N: int):
    res = []
    for i in range(1,N+1):
        if N%i == 0:
            res.append(i)
    return res
def is_prime(N: int):
    res = factors(N)
    if len(res) == 2:
        return True
    else:
        return False
    
print("input number:")
input = int(input())
f = is_prime(input)
print(f)
