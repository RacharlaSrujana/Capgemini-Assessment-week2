'''ATM Simulation'''

def perform(operation,balance):
    print("1.check balance, \n2.deposit, \n3.withdraw, \n4.exit")
    operation=input("Select the operation : ")
    if operation=='1':
        check_balance(operation,balance)
    elif operation=='2':
        deposit(operation,balance)
    elif operation=='3':
        withdraw(operation,balance)
    else:
        exit()

def check_balance(operation,balance):
    print(f"Total balance = {balance}")
    perform(operation,balance)

def deposit(operation,balance):
    deposit_amount=int(input("Enter the amount to deposit : "))
    balance=balance+deposit_amount
    perform(operation,balance)

def withdraw(operation,balance):
    withdraw_amount=int(input("Enter the amount to withdraw : "))
    if balance<withdraw_amount:
        print("Insufficient balance for withdrawal")
    else:
        balance=balance-withdraw_amount
    perform(operation,balance)

def exit():
    print("Hope you enjoyed our services")

balance=100
operation=''
perform(operation,balance)
