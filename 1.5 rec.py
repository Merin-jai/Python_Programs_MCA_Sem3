def recursiveSum(n):
    if n <= 1:
        return n
    return n + recursiveSum(n - 1)

n = 10
print(recursiveSum(n))
