# Exercise 1
name = "Bohdana"
age = 17
age_full = 17.9
is_student = True
is_rich = False
country = "Ukraine"
height = 165.5
is_cool = True
surname = "Porokhovnik"
floor = 9

# Exercise 2
a = 2
b = 5
y = None

y = a
a = b
b = y

print(a)
print(b)

# Exercise 3
x = 3
y = 9

first_formula = 2*x + 3*y
print(first_formula)

second_formula = x**2 + 2*x*y + y**2
print(second_formula)

third_formula = 2/8*x - 13/7*y
print(third_formula)

fourth_formula = y ** ((4*x-2*y)**1/2)
print(fourth_formula)

fifth_formula = x % y
print(fifth_formula)

six_formula = (y/x)**2
print(six_formula)

seven_formula = x > y
print(seven_formula)

eight_formula = x**2 != y
print(eight_formula)

# Exercise 4
name = "alcohol"
price = 100

text = f"{name} дорівнює {price} гривень"
print(text)

# Exercise 5
x1 = 1
x2 = 2
x3 = 3
x4 = 4

check = (x1 > x3) or (x2 > x4) and not (x2 != x3) or (x1 == x4)
print(check)

# Exercise 6
height = float(input("Write your height in cm: "))
weight = float(input("Write your weight in kilos: "))

bmi= (weight**2)/height

print(f"При вазі {weight}кг і рості {height} метрів Ваш BMI складає {bmi}")

from string import digits
# Extra
r_1 = 30
r_2 = 36

S_1 = 3.14 * r_1**2
S_2 = 3.14 * r_2**2

diff =(((S_2-S_1)/S_1))
print(f"Друга піца на {diff:.2%} більша за першу")