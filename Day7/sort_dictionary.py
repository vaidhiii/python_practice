students = {"Aman": 82, "Riya": 95, "Rahul": 70, "Neha": 88}

sorted_students = dict(sorted(students.items(), key=lambda x: x[1]))

print(sorted_students)
