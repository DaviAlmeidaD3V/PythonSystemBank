import textwrap

def menu():
    menu = """\n
    
    Menu BankSystem

    [d]\t Deposit
    [w]\t withdraw
    [e]\t Extract
    [nc]\t New Account
    [lc]\t List Accounts
    [nu]\t New User
    [q]\t Quit

    """
    return input(textwrap.dedent(menu))

def Deposit(balance, value, extract, /):

    if value > 0:

        balance += value

        extract += f'Deposit: \t $ {value:.2f}\n'

        print("\n success in Deposit ")
    else:
        print("\n error in Deposit")

    return balance, extract

def withdraw(*, balance, value, extract, limit, number_withdrawals, limit_withdrawals):

    exceeded_balance = value > balance
    exceeded_limit = value > limit
    exceeded_withdrawals = number_withdrawals > limit_withdrawals

    if exceeded_balance:
        print("you dont have Account balance suficient for withdraw: your money. ")

    if exceeded_limit:
        print("you cannot withdraw more than $ 500 Dolars per day")

    if exceeded_withdrawals:
        print(f"you cannot withdraw more than {MAXIMUM_WITHDRAWALS} times per day")

    elif value > 0:
        balance -= value

        extract += f'Withdraw:\t  $ {value:.2f}\n'

        number_withdrawals += 1

        print("\n success in Withdraw ")

    else:
        print("\n error in Withdraw")

    return balance, extract

def view_withdraw(balance, /, *, extract):
    print("\n ========== Extract ========= ")
    print(" Dont was realized Transations. " if not extract else extract)
    print(f"\nBalance: \t $ {balance:.2f}")

def create_user(users):
    identity = input("Please send your Identity (Only Numbers ) ")
    user = filter_user(identity, users)

    if user:
        print("\nWe already have an account created with this identity")

        return
    
    name = input("Please send your FullName: ")
    birthday = input("Please send your BirthDay (Format: m/d/y  ) ")
    address = input("Please send your address (public place, number House, Neighborhood, City/Acronym State): ")

    users.append({"name": name, "birthday": birthday, "identity": identity, "address": address})

    print("User created with success")

def filter_user(identity, users):
    users_filtered = [user for user in users if user["identity"] == identity]
    return users_filtered[0] if users_filtered else None

def create_account(agency, account_number, users):
    identity = input("Please Send your identity user ")
    user = filter_user(identity, users)

    if user:
        print("\n Created account with success ! ")
        return {"agency": agency, "account number": account_number, "user": user}

    print("\n I didn't find that user. Sorry")

def list_accounts(accounts):
    for account in accounts:
        line = f"""
            Agency:\t{account['agency']}
            C/C::\t{account['account number']}
            Owner of the account:\t{account['user']['name']}
        """
        print(textwrap.dedent(line))

def main():
    MAXIMUM_WITHDRAWALS = 3

    AGENCY = "0001"

    balance = 0
    limit = 500
    extract = ""
    number_withdrawals = 0
    users = []
    accounts = []

    while True:
        option = menu()

        if option == "d":
            value = float(input("info Deposit value: "))

            balance, extract = Deposit(balance, value, extract)

        elif option == "w":
            value = float(input("withdraw value: "))

            balance, extract = withdraw(
                balance=balance,
                value=value,
                extract=extract,
                limit=limit,
                number_withdrawals=number_withdrawals,
                limit_withdrawals=MAXIMUM_WITHDRAWALS,
            )
        
        elif option == "e":
            view_withdraw(balance, extract=extract)

        elif option == "nc":
            account_number = len(accounts) + 1 
            account = create_account(AGENCY, account_number, users)

            if account:
                accounts.append(account)

        elif option == "lc":
            list_accounts(accounts)
    
        elif option == "nu":
            create_user(users)
                
        elif option == "q":
            break

        else:
            print("\nPlease Send one valid Option")

main()