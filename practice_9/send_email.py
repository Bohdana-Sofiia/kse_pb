def send(users, emails):
    sender = input("enter sender: ")
    recipient = input("enter recipient")
    mail = input("enter text: ")
    if recipient not in users:
        print("Recipient is not registrated")
    else:
        emails.append({"sender": sender, "recipient": recipient, "email": mail})