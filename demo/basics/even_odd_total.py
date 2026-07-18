# Take 5 numbers and print total of even numbers and odd numbers

even_total = odd_total =  0

for n in range(5):
    num = int(input("Enter a number :"))
    if num % 2 == 0:
        even_total += num
    else:
        odd_total += num


print(f'Even Total :{even_total}, Odd Total : {odd_total}')