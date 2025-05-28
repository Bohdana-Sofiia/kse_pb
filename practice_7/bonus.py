import random
import matplotlib.pyplot as plt

a_price = 100
b_price = 200
c_price = 300

start = 10000
a_invest = start * 0.4
b_invest = start * 0.3
c_invest = start * 0.3

a_shares = a_invest / a_price
b_shares = b_invest / b_price
c_shares = c_invest / c_price

a_values = []
b_values = []
c_values = []
portfolio = []

for month in range(1, 25):
    # Зміна цін для кожної акції
    a_change = random.uniform(-0.05, 0.07)
    b_change = random.uniform(-0.05, 0.07)
    c_change = random.uniform(-0.05, 0.07)

    a_price *= (1 + a_change)
    b_price *= (1 + b_change)
    c_price *= (1 + c_change)

    a_values.append(a_price)
    b_values.append(b_price)
    c_values.append(c_price)

    a_val = a_shares * a_price
    b_val = b_shares * b_price
    c_val = c_shares * c_price

    portfel_value = a_val + b_val + c_val
    portfolio.append(portfel_value)

    print(f"Місяць {month}: портфель = {portfel_value:.2f} грн")

print(f"Максимальна вартість портфеля: {max(portfolio):.2f} грн")
print(f"Мінімальна вартість портфеля: {min(portfolio):.2f} грн")

returns = []
for i in range(1, len(portfolio)):
    r = (portfolio[i] - portfolio[i-1]) / portfolio[i-1]
    returns.append(r)

avg_return = sum(returns) / len(returns)
print(f"Середня місячна дохідність: {avg_return * 100:.2f}%")

plt.plot(portfolio)
plt.show()
