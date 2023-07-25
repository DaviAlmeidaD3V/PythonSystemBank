PainelSystem = """

    [d] Deposit
    [s] To withdraw
    [e] Extract
    [q] Quit

"""


Account_Balance = 0

Withdrawal_Limit = 500

Account_Statement = ""

Withdrawal_Numbers = 0

Maximum_Withdrawals = 3

while True:

    Option = input(PainelSystem)

    if Option == "d":
        Value = int(input('deposit amount to be credited: '))

        Account_Statement += f'deposit $ {Value:.2f} in your account\n'

        if Value < 0:
            print("your deposit can't be negative ")
        else:
            Account_Balance += Value

    
    elif Option == "s":
        Withdrawal_Numbers += 1

        Withdrawal_Value = int(input('Value of Withdrawal: '))

        Exceeded_Limit = Withdrawal_Value > Withdrawal_Limit

        Exceeded_Withdrawals = Withdrawal_Numbers > Maximum_Withdrawals

        Exceeded_Account_Balance = Withdrawal_Value > Account_Balance


        if Exceeded_Limit:
            print(f'you cannot withdraw more than {Withdrawal_Limit:.2f} per day')

        elif Exceeded_Withdrawals:
            print(f'you cannot withdraw more than {Maximum_Withdrawals} times per day')
            

        elif Exceeded_Account_Balance:
            print(f'you dont have Account balance suficient for withdraw: your money {Account_Balance:.2f}')

        else:
            Account_Statement += f'voce retirou R$ {Withdrawal_Value:.2f} da sua conta\n'
            Account_Balance -= Withdrawal_Value


    elif Option == "e":
        if Account_Balance > 0:
            print("------------------------------------------")
            print(f'{Account_Statement}')
            print("------------------------------------------")
        else:
            print("your account is empty: ")
    

    elif Option == "q":
        break

    else:
        print("invalid option choose a correct option: ")
