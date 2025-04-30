def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

def reverse_and_add(n):
    count = 0
    while n != reverse_number(n):
        n += reverse_number(n)
        count += 1
    return n, count

# Take input from the user
number = int(input("Enter a number: "))
result, count = reverse_and_add(number)  # Unpack the returned values

print("Palindrome after reverse and add:", result)
print("Number of iterations:", count)
