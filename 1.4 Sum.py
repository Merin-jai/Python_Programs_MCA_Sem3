def div():
    count = 0
    total_sum = 0
    for num in range(101, 200):
        if num % 7 == 0:
            count += 1
            total_sum += num
    return count, total_sum

count, total_sum = div()
print("Count of numbers divisible by 7:", count)
print("Sum of numbers divisible by 7:", total_sum)
