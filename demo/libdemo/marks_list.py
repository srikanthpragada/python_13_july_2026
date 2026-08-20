f = open("students.txt", "rt")

for line in f.readlines():
    parts = line.split(",")
    if len(parts) < 2:
        continue

    name = parts[0]
    marks = [int(m) for m in parts[1:]]

    total = sum(marks)
    avg = total / len(marks)

    print(f"{name:20} {total:3} {avg:.2f}")

f.close()
