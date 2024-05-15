pwd = input("What is your master password? ")

while True:
    mode = input("Would you like to add a new password or retrieve an existing one (view, add)(q to quit)? ").lower
    if mode == "q":
        break
    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode selected.")
        continue
