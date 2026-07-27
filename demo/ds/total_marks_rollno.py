data = [(1, 60), (2, 70), (1, 80), (3, 55), (2, 90)]

students = {}

for rollno, marks in data:
    total = students.get(rollno, 0)
    students[rollno] = total + marks

print(students)


