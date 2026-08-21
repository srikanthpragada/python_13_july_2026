f = open("names.txt", "rt")
name = input("Enter name :")
found = False
while True:
    line = f.readline().strip()
    if line == "":   # EOF
        break

    if line.lower() == name.lower():
        print("Found!")
        found = True
        break

f.close()

if not found:
    print('Not found!')


