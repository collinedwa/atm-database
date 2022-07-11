from banking_pkg import account
import pandas as pd

# Stores user database as variable
user_accounts = pd.read_csv("user_accounts.csv")


def user_register():
    global user_accounts
    while True:
        name = input("Enter name to register: ")
        # Check to see if username is already registered in database
        if name in user_accounts['name'].unique():
            print("Username taken! Please enter a different name.\n")
            continue
        if len(name) > 10:
            print("Name must be under 10 characters\n")
            continue
        elif len(name) == 0:
            print("Please enter a name\n")
            continue
        try:
            int(name)
            print("Name should be letters only!\n")
            continue
        except:
            pass
        break

    while True:
        pin = input("Enter PIN: ")
        if len(pin) != 4:
            print("PIN length must be 4!\n")
            continue
        try:
            int(pin)
            break
        except TypeError:
            print("PIN should only contain numbers\n")
            continue
    print(f"{name} has been registered with a starting balance of $0.00\n")
    # Creates a new user based on entered information and writes it to database
    new_user = pd.DataFrame([{"name": name, "pin": pin, "balance": 0.00}])
    user_accounts_new = pd.concat([user_accounts, new_user], ignore_index=True, join="inner")
    user_accounts_new.to_csv("user_accounts.csv")

    # Refreshes database variable
    user_accounts = pd.read_csv("user_accounts.csv")


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


while True:
    print("          === Automated Teller Machine ===          \n")
    print("------------------------------------------")
    print("| 1. Existing User  | 2.    New User     |")
    print("------------------------------------------")
    existing_user = input("Choose an option: ")

    if existing_user == '1':
        break
    elif existing_user == '2':
        user_register()
        break
    else:
        print("Invalid choice!\n")
        continue


login = False
while login is False:
    name_test = input("Enter name to login: ")
    pin_test = input("Enter PIN to login: ")
    # Check to confirm user exists in database, and entered pin matches the stored user pin
    if name_test in user_accounts['name'].unique() and user_accounts[user_accounts["name"] == name_test]["pin"].iloc[0] == int(pin_test):
        print("Login successful!")
        login = True
        current_user = {"name": name_test, "pin": pin_test, "balance": user_accounts[user_accounts["name"] == name_test]["balance"].iloc[0]}
        break
    elif name_test not in user_accounts['name'].unique():
        print("User does not exist!")

        while True:
            user_choice = input("Would you like to create a new account? (Y/N): ")
            if user_choice.upper() == 'Y':
                user_register()
                break
            elif user_choice.upper() == 'N':
                break
            else:
                print("Invalid input!")
                continue

    else:
        print("Login failed!")
        continue

# Updates the local balance to a retrieved balance from user database
balance = current_user["balance"]

while login is True:
    atm_menu(current_user["name"])
    option = input("Choose an option: ")
    if option == '1':
        account.show_balance(balance)
    elif option == '2':
        balance = account.deposit(balance)
    elif option == '3':
        balance = account.withdraw(balance)
    elif option == '4':
        account.logout(current_user["name"])

        # Updates balance information and saves it to database
        current_user_index = user_accounts[user_accounts["name"] == current_user["name"]].index.values.astype(int)[0]
        user_accounts.at[current_user_index, "balance"] = balance
        user_accounts.to_csv("user_accounts.csv", index=False)
        login = False
    else:
        print('Invalid input!')
        continue