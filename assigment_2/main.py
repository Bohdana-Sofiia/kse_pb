# Завдання 1
hello = "Hello, Python World!"
print(hello)

# Завдання 2
num_1 = int(input("Write first number:"))
num_2 = int(input("Write second number:"))

print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2) 

# Завдання 3
text_1 = "Hello"
text_2 = "World"
full_text = text_1 + text_2
print(f"{full_text} has {len(full_text)} letters")

#Завдання 4

num = int(input("Say a number bro: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Завдання 5
numbers = 0
while numbers < 10:
    numbers += 1
    print(numbers)

# Завдання 6
number = float(input("Write a number again bro: "))
if number > 0 :
    print("Positive!")
elif number == 0:
    print("Zero, just like Cola")
else:
    print("Negative bro:(")

# Завдання 7
for i in range(2, 11, 2):
    print(i)

# Завдання 8
n = int(input("Write a number: "))
total = 0
for i in range (1, n+1):
    total += i
print(f"sum is {total}")
    
# Завдання 9
for i in range(10, 0, -1):
    print(i)

# Завдання 10
for i in range(1, 11):
    if i == 5:
        continue
    elif i == 7:
        break
    print(i)