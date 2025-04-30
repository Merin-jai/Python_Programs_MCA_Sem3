def pyramid(n):
    for i in range(n):
        spaces = " " * (n - i - 1)  # Create the spaces
        symbols = "+ " * (i + 1)    # Create the plus symbols
        print(spaces + symbols)     # Print spaces followed by plus symbols

pyramid(6)
