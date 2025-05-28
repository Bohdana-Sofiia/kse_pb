# 1
user_text = input("Enter some text")
letters_count = {}
letters_to_ignore = [" ", "@", ",", ".", "!", "?"]
for letter in user_text:
  if letter in letters_to_ignore:
    continue

  if letter in letters_count:
    letters_count[letter] += 1
  else:
    letters_count[letter] = 1
print(letters_count)

#2
n = int(input("Give a num bro: "))
result = []
def even_square(n):
  for i in range(n+1):
    if i % 2 == 0:
      i = i**2
      result.append(i)
  return result
print(even_square(n))

#3
dictionary_1 = {}
for key in range(1,11):
  empty = []
  for key2 in range(1,11):
    new_value = key * key2
    empty.append(new_value)
  dictionary_1[key] = empty
print(dictionary_1)

#4
cities = "Tokyo Seoul London Sofia Tokyo Sydney London".split(" ")
empty = {}
for i in cities:
  if i in empty:
    empty[i] += 1
  else:
    empty[i] = 1
max_num = max(empty.values())
ls = []
for key, values in empty.items():
  if values == max_num:
    ls.append(key)
print(min(ls))

#5
S = float(input("Give sum "))
r = float(input("give rate "))
n = int(input("Give monthes "))
balance = 0

for i in range(n):
  balance = S*((((1+r)**n)-1)/r)
print(balance)

#6
expenses = {
    "Понеділок": 350,
    "Вівторок": 400,
    "Середа": 300,
    "Четвер": 500,
    "П’ятниця": 450,
    "Субота": 700,
    "Неділя": 600
}

sum_ex = sum(expenses.values())
print(sum_ex)
max_day = max(expenses.values())
for key, value in expenses.items():
    if value == max_day:
        print(f"Найбільше витрачено: {key} - {value}грн")

avr = round(sum(expenses.values()) / len(expenses), 2)
print(f"Середні витрати: {avr} грн")

#7
import random

results = ["Скарб! Ви виграли 100 золотих!", "Пастка! Ви втратили життя.", "Монстр! Ваша втеча не вдалася."]
cont = input("Do you want to continue playing? ")
wins = 0
loses = 0
while cont != "no":
  choose = int(input("Choose a door 1, 2 or 3: "))
  random.shuffle(results)
  result = results[choose-1]
  if result == "Скарб! Ви виграли 100 золотих!":
    wins += 1
  if result != "Скарб! Ви виграли 100 золотих!":
    loses += 1
  print(result)
  cont = input("Do you want to continue playing? ")
print(f"You win {wins} times, you lose {loses} times")

#bonus
import random
import matplotlib.pyplot as plt
import math

x, y = 0, 0
movement = [(x,y)]
steps = int(input("Write amount of steps bro: "))

for i in range(steps):
  direction = random.choice(["up", "down", "left", "right"])
  if direction == "up":
    y += 1
  if direction == "down":
    y -= 1
  if direction == "left":
    x -= 1
  if direction == "right":
    x += 1
  movement.append((x,y))
end_point = movement[-1]
distance = math.sqrt(end_point[0]**2 + end_point[1]**2)
print(movement)
print(end_point, distance)


plt.plot(*zip(*movement))
plt.xlabel('X')
plt.ylabel('Y')
plt.show() 