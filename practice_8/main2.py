from data import inventory, transactions
from add_product import add_product
from buy_product import buy_product

while True:
    what_to_do = int(input("1 — додати товар, 2 — купити товар, 3 — переглянути облік, 0 — вийти: "))
    if what_to_do == 0:
        break
    if what_to_do == 1:
        name = input("Який товар ти хочеш? ")
        quantity = int(input("Скільки бро? "))
        add_product(inventory, name, quantity)
    if what_to_do == 2:
        name = input("Який продукт хочеш купити?")
        quantity = int(input("Скільки бро? "))
        seller_id = int(input("Хто продав? "))
        buy_product(inventory, transactions, name, quantity, seller_id)
    if what_to_do == 3:
        pass
    if what_to_do == 4:
        pass
