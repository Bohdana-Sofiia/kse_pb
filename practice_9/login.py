import hashlib

def login(users):
    name = input("Write a name: ")
    print(users)
    print(name, users)
    password = input("Write a password: ")
    password_hash = hashlib.sha256("{}".format(password).encode()).hexdigest()
    if name not in users:
        print("You are not registrated")
    else:
        if password_hash == users[name]:
            print("You are loggen in")
            return True, name
    return False, None