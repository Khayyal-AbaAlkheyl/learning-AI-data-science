class BalanceException(Exception):
    pass



class Bank_account:
    def __init__(self,intial_amount,account_name):
        self.balance=intial_amount
        self.name=account_name
        print(f"\naccont '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"account '{self.name}' balance = {self.balance:.2f}")
        
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"\nDeposit compelet.")
        self.getBalance()
    def viableTransaction(self,amount):
        if self.balance>=amount:
            return 
        else :
            raise BalanceException(f"\nSorry, account {self.name} has only a balance of {self.balance:.2f}")
    
    def withdaw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance=self.balance-amount
            print("\nwithdraw compelte.")
            self.getBalance()
        except BalanceException as error :
            print(f"withdraw interrupted: {error}")
    def transfor(self, amount , account):
        try:
            print(f"**********\n\nBeginning Transfer..")
            self.viableTransaction(amount)
            self.withdaw(amount)
            account.deposit(amount)
            print(f"\nTransaction compelete.\n\n**********")
        except BalanceException as error:
            print(f"transaction interrupted: {error}")


class IntersetRewardAccount(Bank_account):
    def deposit(self, amount):
       self.balance=self.balance+(amount*1.05)
       print("Deposit compelte")
       self.getBalance()

class SavingsAcount(IntersetRewardAccount):
    def __init__(self, intial_amount, account_name):
        super().__init__(intial_amount, account_name)
        self.fee=5

    def withdaw(self, amount):
       try:
           self.viableTransaction(amount + self.fee)
           self.balance =self.balance - (amount + self.fee)
           print("\nwithdraw compelet.")
           self.getBalance()

       except BalanceException as error:
              print(f"withdraw interrupted: {error}")