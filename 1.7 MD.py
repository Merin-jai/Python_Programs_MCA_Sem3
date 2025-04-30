ch = int(input("1. Check String is Substring of Another String\n"
               "2. Count Occurrences of Character\n"
               "3. Replace a substring with another substring\n"
               "4. Convert to Capital Letters\n"
               "Enter your choice: "))

if ch == 1:
    a = input("Enter a string: ")
    b = input("Enter another string: ")
    if b in a:  # Check if b is a substring of a
        print("Substring is present.")
    else:
        print("Substring is not present.")

elif ch == 2:
    a = input("Enter a string: ")
    b = input("Enter a character for checking their occurrences: ")
    count = a.count(b)  # Use count method for simplicity
    print("Count is", count)

elif ch == 3:
    a = input("Enter a string: ")
    b = input("Enter a substring to replace: ")
    c = input("Enter a substring for replacing: ")
    if b in a:  # Check if b is a substring of a
        y = a.replace(b, c)
        print("Updated string:", y)
    else:
        print("No such substring.")

elif ch == 4:
    a = input("Enter a string: ")
    print("In capital letters:", a.upper())

else:
    print("Invalid choice.")
