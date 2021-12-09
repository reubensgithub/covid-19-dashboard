def vat(pretax_price, kids=False, category='Miscellaneous'):
    if isinstance(pretax_price, str): # if pretax_price is a string, convert it to an int
        pretax_price = int(pretax_price)
    if pretax_price < 0:
        return pretax_price
    if category == 'food' or (category == 'clothing' and kids):
        return pretax_price
    return pretax_price * 1.2


vat(100, False, 'Miscellaneous')