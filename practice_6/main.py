# Завдання 1
import geometry

print(geometry.rectangle_area(4,6))

# Завдання 2
import converter

print(converter.uah_to_usd(1000, 39.5))
print(converter.usd_to_uah(1000, 39.5))

# Завдання 3
import taxes

revenue = 15000
vat = taxes.calculate_vat(revenue)
tax = taxes.calculate_income_tax(revenue)
taxes = vat + tax
print(taxes)

# Завдання 4
import math
print(math.sqrt(121))
print(math.sin(math.pi/2))
print(math.floor(7.8))
print(math.ceil(7.8))

# Завдання 5
import random
cube_1 = random.randint(1, 6)
cube_2 = random.randint(1, 6)

print(cube_1)
print(cube_2)
print(cube_1 + cube_2)

# Завдання 6
import datetime

date_birth = input("Write your birthdate: ")

birthdate = datetime.datetime.strptime(date_birth, "%Y-%m-%d")
today = datetime.date.today()

days_lived = (today -birthdate.date()).days
print(f"You are living for {days_lived} days")

#Завдання 7
import random

start_balance = 10000
stavka = 100
iter_count = 0
while start_balance >= 100 or iter_count <= 1000:
    iter_count += 1
    number = random.random(0, 1)
    if number <= 1/37:
        win = start_balance + 1/number*stavka
        break
    else:
        lose = start_balance - stavka