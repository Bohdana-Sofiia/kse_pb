from utils import is_valid_price, is_valid_quantity

def buy_product(inventory, transactions, name, quantity, seller_id):
    is_valid_quantity(quantity)
    if name in inventory:
        if quantity > inventory[name]["quantity"]:
            print("Вибачте, недостатньо товарів")
        else:
            inventory[name]["quantity"] -= quantity
            price = inventory[name]["price"]*quantity
            transactions.append({"name": name, "quantity": quantity, "price": price})
            print(f"Сума до сплати:{price}")
    else:
        print("Таких речей немає")
    return transactions

#def print_check(n = 1):
    