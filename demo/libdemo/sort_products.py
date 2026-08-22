import json

with open("products.json") as f:
    products = json.load(f)


sorted_products = sorted(products, key = lambda d : d['price'])

for prod in sorted_products:
    discount = prod['price'] * prod['discount'] // 100
    price = prod['price']
    net_price = price - discount
    print(f"{prod['name']:20} {price:6} {discount:6} {net_price:6}")



