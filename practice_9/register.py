import hashlib

def registration(users):
    login = input("Enter your login: ")
    password = input("Enter a password: ")
    password_hash = hashlib.sha256("{}".format(password).encode()).hexdigest()
    if login in users:
        print("Username is already taken")
    else:
        users.update({login: password_hash})    