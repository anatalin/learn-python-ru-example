def format_price(price):
    price_int = int(price)
    return f'Цена: {price_int} руб.'

result = format_price(56.42)
print(result)