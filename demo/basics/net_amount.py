# Take qty and price and display net amount

qty = int(input("Enter qty : "))
price = int(input("Enter price : "))
amount = qty * price
if qty > 2:
    discount = amount * 20 // 100
else:
    discount = amount * 10 // 100

net_amount = amount - discount

print(f'Amount      : {amount:6}')
print(f'- Discount  : {discount:6}')
print(f'Net Amount  : {net_amount:6}')
