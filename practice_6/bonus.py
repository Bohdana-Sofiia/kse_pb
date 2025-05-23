import random
import matplotlib.pyplot as plt

start_balance = 10000
stavka = 100
iter_count = 0
history = [start_balance]
while start_balance >= 100 and iter_count <= 1000:
    iter_count += 1
    number = random.random()
    if number <= 1/37:
        start_balance = start_balance + 36*stavka
    else:
        start_balance = start_balance - stavka
    history.append(start_balance)

plt.plot(history)
plt.show()