students = {
    "Aman": 82,
    "Riya": 91,
    "Karan": 67,
    "Priya": 88,
    "Neha": 75
}

topper = max(students.items(), key=lambda x: x[1])
print("Topper is: ",topper)

lowest = min(students.items(), key=lambda x: x[1])
print("Lowest scorer: ",lowest)

sort= sorted(students.items(), key= lambda x: x[1])
print("Sorted Dictionary: ",sort)

print("Did all students passed:")
print(all(mark>=35 for mark in students.values()))

print("Did any student scored above 90:")
print(any(mark >90 for mark in students.values()))

average=sum(students.values()) / len(students) 
print("Average marks: ",average)