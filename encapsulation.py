class bank:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
    def check_balance(self):
        print(f"Account Balance is :{self.__balance}")
    def deposite(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if self.__balance<amount:
            print("Insufficient balance")
            return
        self.__balance-=amount
        print(f"Withdraw successfully: {self.__balance}")
a=bank(123,30000)
a.check_balance()
a.withdraw(3000)
a.deposite(20)