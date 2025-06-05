from data import emails, users
from register import registration
from login import login
from logout import logout
from send_email import send
import hashlib

user_status = False
while True:
    try:
        start = int(input("0 - exit, 1 - sign up, 2 - login, 3 - send, 4 - logout: "))
    except Exception as e:
        print(e)
        start = None
    if start == 0:
        break
    elif start == 1:
        if user_status is False:
            registration(users)
        else:
            print("You are logged in")
    elif start == 2:
        if user_status is False:
            user_status = login(users)
        else:
            print("You are logged in")
    elif start == 3:
        print(user_status)
        if user_status is True:
            send(users, emails)
        else:
            print("You are not logged in to send email")
    elif start == 4:
        if user_status is True:
            user_status = logout()
        else:
            print("You are not logged in to logout")
        print("logout")
    elif start == 5:
        print(users)
