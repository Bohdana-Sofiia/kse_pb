# Завдання 1
nums = [3, 7, 2, 9, 5]

average = sum(nums)/len(nums)
print(average)

# Завдання 2
nums = [4, 7, 2, 4, 8, 9, 2, 10, 3, 8]

unique_set = set(nums)
unique_set2 = list(unique_set)
even_num = []

for num in unique_set2:
  if num % 2 == 0:
    even_num.append(num)
even_num = sorted(even_num, reverse=True)
print(even_num)

# Завдання 3
grades = [
    [90, 85, 88],
    [75, 80, 79],
    [95, 92, 96],
    [88, 85, 84]
]

empty_set = []

for row in grades:
  value = sum(row)/len(row)
  empty_set.append(value)

max_value = max(empty_set)

for i, mark in enumerate(empty_set):
  if mark == max_value:
    break
print(i)
print(mark)
print(grades[2])

# Завдання 4
prices = {
    "apple": 12,
    "banana": 8,
    "milk": 25,
    "bread": 20
}

price = list(prices.values())
sum_price = sum(price)
print(sum_price)

# Завдання 5
people = {
    "Anna": "Kyiv",
    "Bohdan": "Lviv",
    "Oksana": "Kyiv",
    "Dmytro": "Odesa"
}

all_values = list(set(people.values()))
empty_values = {}
for i in all_values:
  empty_values[i] = []

for key, value in people.items():
  empty_values[value].append(key)
print(empty_values)

# Завдання 6
data = {
  "user_001": {
    "transactions": [
      {
        "details": {
          "transaction_id": "TXN00001",
          "amount": 123.45,
          "currency": "USD"
        },
        "meta": {
          "timestamp": "2024-04-10T14:22:01",
          "status": "completed",
          "category": "groceries"
        },
        "bank_noise": {
          "bank_code": "BANK_US_001",
          "terminal_id": "TRM1023",
          "merchant_name": "WholeMart City Center"
        }
      },
      {
        "details": {
          "transaction_id": "TXN00002",
          "amount": 89.99,
          "currency": "USD"
        },
        "meta": {
          "timestamp": "2024-06-25T09:11:45",
          "status": "pending",
          "category": "services"
        },
        "bank_noise": {
          "bank_code": "BANK_US_002",
          "terminal_id": "TRM1147",
          "merchant_name": "QuickFix Repairs"
        }
      },
      {
        "details": {
          "transaction_id": "TXN00003",
          "amount": 345.0,
          "currency": "USD"
        },
        "meta": {
          "timestamp": "2024-08-17T18:05:33",
          "status": "completed",
          "category": "electronics"
        },
        "bank_noise": {
          "bank_code": "BANK_EU_008",
          "terminal_id": "TRM2011",
          "merchant_name": "TechStore EU"
        }
      },
      {
        "details": {
          "transaction_id": "TXN00004",
          "amount": 59.1,
          "currency": "USD"
        },
        "meta": {
          "timestamp": "2024-11-03T20:14:27",
          "status": "failed",
          "category": "entertainment"
        },
        "bank_noise": {
          "bank_code": "BANK_US_004",
          "terminal_id": "TRM1455",
          "merchant_name": "MovieZone Downtown"
        }
      },
      {
        "details": {
          "transaction_id": "TXN00005",
          "amount": 210.75,
          "currency": "USD"
        },
        "meta": {
          "timestamp": "2024-12-19T08:47:52",
          "status": "completed",
          "category": "clothing"
        },
        "bank_noise": {
          "bank_code": "BANK_CA_005",
          "terminal_id": "TRM3320",
          "merchant_name": "FashionLoop Toronto"
        }
      }
    ]
  }
}

status = {}
trans = data['user_001']["transactions"]
for i in trans:
  amount = i["details"]["amount"]
  st = i["meta"]["status"]
  if st not in status:
    status[st] = amount
  else:
    status[st] = status[st] + amount

print(status)

#