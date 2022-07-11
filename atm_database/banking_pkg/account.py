def show_balance(balance):
    balance_display = balance_formatter(balance)
    print(f"Balance: {balance_display}")
    return balance


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    try:
        float(amount)
    except TypeError:
        print("Input must be a dollar amount!")
    balance += round(float(amount), 2)
    return balance


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    if float(amount) > balance:
        print("Not enough money in account!")
        return balance
    else:
        balance -= float(amount)
        return balance


def logout(name):
    print(f"Goodbye, {name}!")


def balance_formatter(balance):
    balance_check = str(balance).split('.')
    if len(balance_check[1]) == 1:
        return f"${balance}0"
    elif len(balance_check[1]) > 2:
        balance_check[1] = balance_check[1][:2]
        balance = '.'.join(balance_check)
        return f"${balance}"
    else:
        return f"${balance}"
