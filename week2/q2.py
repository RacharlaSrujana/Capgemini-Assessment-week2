'''Design a `BankAccount` class with `deposit()` and `withdraw()` methods. Implement logic to prevent overdraft.'''

class BankAccount:
    initial_balance=100
    # def __init__(self,deposit_amnt,withdraw_amnt):
    #     self.deposit_amnt=deposit_amnt
    #     self.withdraw_amnt=withdraw_amnt
    def deposit(self,amnt):
        BankAccount.initial_balance+=amnt
        print(f"Total balance : {BankAccount.initial_balance}")
    def withdraw(self,amnt):
        BankAccount.initial_balance-=amnt
        print(f"Total balance : {BankAccount.initial_balance}")

while True:
    b=BankAccount()
    op=input("1.Deposit 2.Withdraw 3.exit\nYour option : ")
    if op=='1':
        amnt=int(input("Enter the amount you want to deposit : "))
        b.deposit(amnt)
    elif op=='2':
        amnt=int(input("Enter the amount you want to withdraw : "))
        b.withdraw(amnt)
    elif op=='3':
        print("Thankyou")
        break
