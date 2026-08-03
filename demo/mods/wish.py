import sys

#print(sys.argv)
if len(sys.argv) < 2:
    print('Name is missing!')
    exit()

user = sys.argv[1]
print("Hello", user)
