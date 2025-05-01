def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

n = int(input("Enter a number: "))
factorial_value = fact(n)
print(f"The factorial of {n} is: {factorial_value}")

result_dict = {"The factorial is": factorial_value}
print(result_dict)
