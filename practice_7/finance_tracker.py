
transactions = []

def add_transaction(transactions, amount, trans_type, category):
    transaction = {"amount": amount, "trans_type": trans_type,"category": category}
    transactions.append(transaction)
    return transactions

add_transaction(transactions, 10000, "дохід", "зарплата")
add_transaction(transactions, 2500, "витрата", "їжа")
add_transaction(transactions, 1500, "витрата", "транспорт")

def get_balance(transactions):
    balance = 0
    for transaction in transactions:
        if transaction["trans_type"] == "дохід":
            balance += transaction["amount"]
        if transaction["trans_type"] == "витрата":
            balance -= transaction["amount"]
    return balance

print(get_balance(transactions))