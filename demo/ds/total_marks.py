
data = "98,77,65,92,A,45"

marks = data.split(",")

total = 0
for m in marks:
    if m.isdigit():
        total += int(m)

print(total)
