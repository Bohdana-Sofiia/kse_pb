# Завдання 1
def calculate_vat(price):
  pdv = 0.2
  res = price * pdv
  return res
result = calculate_vat(100)
print(result)

# Завдання 2
def usd_to_uah(amount):
  ex_rate = 39.5
  usd = amount * ex_rate
  return usd

result = usd_to_uah(100)
print(result)

# Завдання 3
def monthly_salary(hours, rate):
  wage = hours * rate
  return wage

result = monthly_salary(40,30)
print(result)

# Завдання 4
def apply_discount(price, discount):
  new_price = price - price*discount
  return new_price

result = apply_discount(250,0.15)
print(result)

# Завдання 5
def profit(revenue, cost, tax):
  profit_1 = revenue - (cost + tax)
  return profit_1

result = profit(1000,300,150)
print(result)

# Завдання 6
def weighted_average_price(prices, quantities):
  pr_q = 0
  for i, price in enumerate(prices):
    pr_q += prices[i] * quantities[i]
  do = sum(quantities)
  av = pr_q/do
  return av
result = weighted_average_price([10,15,20], [2,3,4])
print(result)

# Завдання 7
def calculate_wacc(equity, debt, cost_of_equity, cost_of_debt, tax_rate):
  wacc = equity/(equity + debt)*cost_of_equity + debt/(equity + debt)*cost_of_debt*(1-tax_rate)
  return wacc

result = calculate_wacc(10,15,30,14,10)
print(result)

# Завдання 8
def monthly_payment(present_value, rate, months):
  c = (present_value*rate)/(1-1/(1+rate)**months)
  return c

result = monthly_payment(1000, 0.5, 12)
print(result)

# Завдання 9
def analyze_prices(prices):
  min_v = min(prices)
  max_v = max(prices)
  avr = sum(prices)/len(prices)
  count = 0
  for i in prices:
    if i < avr:
      count += 1
  new = {}
  new["min"] = min_v
  new["max"] = max_v
  new["avr"] = avr
  new["amount"] = count
  return new

result = analyze_prices([10, 15, 30])
print(result)

# Бонусне
def adjust_for_inflation(income, inflation_rates):
  new_incomes = []
  for rate in inflation_rates:
    income = income + (income * rate)
    new_incomes.append(income)
  return new_incomes
result = adjust_for_inflation(10000, [0.08, 0.1, 0.07])
print(result)

