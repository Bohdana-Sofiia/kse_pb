from utils import is_valid_price, is_valid_quantity

def add_product(inventory, name, quantity):
    is_valid_quantity(quantity)
    if name in inventory:
        inventory[name]["quantity"] += quantity
    else:
        price = int(input("Яка ціна: "))
        is_valid_price(price)
        inventory[name] = {"price": price, "quantity": quantity}
    return inventory