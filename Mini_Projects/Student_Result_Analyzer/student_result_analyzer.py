students = ["Aman", "Riya", "Karan", "Priya"]
marks = [85, 91, 67, 78]

# combine names and marks
result = list(zip(students, marks))
print("Combined List:")
print(result)

# print each students result

print("\nStudents Results:")
for name, mark in result:
    print(f"{name} : {marks}")

# shows students scoring above 80

print("\nStudents scoring above 80:")
for name, mark in result:
    if mark > 80:
        print(name, "-", marks)

# creating dictionary

student_dict = dict(zip(students, marks))
print("\nStudent dictionary:")
print(student_dict)

# Finding topper

topper = max(student_dict, key=student_dict.get)
print("\nTopper:")
print(topper, "-", student_dict[topper])
