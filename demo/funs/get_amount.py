def get_amount(**kwargs) -> int | None:
    qty = kwargs.get('qty', 1)
    price = kwargs.get('price', None)
    if price is None:
        return None
    else:
        return price * qty


print(get_amount(qty = 5, price = 150, discount = 10))
print(get_amount(price = 150))
print(get_amount(qty = 5, rate = 150))


