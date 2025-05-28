import string
import random


def generate_password(length, allow_symbols):
        if allow_symbols == False:
            symbols = string.ascii_letters + string.digits
            password = "".join(random.choices(symbols, k=length)) 
            return password
        if allow_symbols == True:
            symbols = string.ascii_letters + string.digits + string.punctuation 
            password = "".join(random.choices(symbols, k=length))
            return password

print(generate_password(12, True))