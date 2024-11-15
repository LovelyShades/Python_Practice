master_pwd = input("\nPlease type the password to start: \n")

def add():
    name = input('\nusername: \n')
    pwd = input('\npassword: \n')

    with open('password_test.txt', 'a') as f:
        f.write(name + "|" + pwd)


def view():
    pass

while True:
    mode = input("\nWould you like to.. \n\na) add a new password\nb) view existing passwords\n--------------------------\npress \"q\" to quit \n\n")
    if mode == "q":
        break

    if mode == "a":
        add()

    elif mode == "b":
        view()

    else:
        print("Invalid input. Please try again")
        continue