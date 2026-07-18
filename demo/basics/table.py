# take a number and display table

num = int(input("Enter a number :"))

for i in range(1, 11):
    print(f"{num:3} * {i:2} = {num * i:5}")

