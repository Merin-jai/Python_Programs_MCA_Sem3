n = int(input("Enter number of students: "))   
result = {}

# Collecting student details
for i in range(n):   
    print("Enter Details of student No.", i + 1)   
    roll = int(input("Enter Roll No: "))   
    name = input("Enter Name: ")   
    mark = int(input("Enter total marks secured: "))   
    result[roll] = [name, mark]     

# Printing all results
print(result)

# Finding the student with the highest mark
highest_student = None
highest_mark = -1

for student in result.values():   
    if student[1] > highest_mark:
        highest_mark = student[1]
        highest_student = student[0]

if highest_student:
    print("Student with the highest mark:", highest_student)
else:
    print("No student has secured marks.")
