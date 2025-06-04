def is_valid_price(value):
    if value > 0:
        return True
    return False

def is_valid_quantity(value):
    if value > 0:
        return True
    return False

def format_currency(amount):
    amount = (f"{amount}грн")
    return amount
