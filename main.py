from cryptography.fernet import Fernet

pwd = input("What is your master password? ")


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)


def add():
    name = input("What is the name of the account? ")
    pwd = input("What is the password? ")

    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + pwd + "\n")


while True:
    mode = input("Would you like to add a new password or retrieve an existing one (view, add)(q to quit)? ")
    mode.lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode selected.")
        continue
