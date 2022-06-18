class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate/100
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance: ${self.balance}")
        return self


    def withdraw(self, amount):
        if self.balance-amount > 0:
            self.balance -= amount
            print(f"Balance: ${self.balance}")
            return self
        else:
            self.balance -= 5
            print(f"Insufficient funds: Charging a $5 fee. Balance: {self.balance}")
            return self


    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance*self.int_rate
            print(f"Balance: ${self.balance}")
            return self
    
bankAccount1 = BankAccount(50)
bankAccount2 = BankAccount(1)

bankAccount1.deposit(100).deposit(200).deposit(300).yield_interest()
bankAccount2.deposit(1000).deposit(300).withdraw(100).withdraw(700).withdraw(800).withdraw(200).yield_interest()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            "account1" : BankAccount(int_rate=2, balance=0),
            "account2" : BankAccount(5, 100)
        }
    
    def make_deposit(self, amount):
        print(f"{self.name} did a deposit")
        self.account['account1'].deposit(amount)
        return self

    def make_withdrawl(self, amount):
        print(f"{self.name} did a withdrawl")
        self.account['account1'].withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"{self.name} account details")
        self.account['account1'].display_account_info()
        return self
        
vesa = User("Vesa", "vesaberdyna@gmail.com")
vesa.make_deposit(1000).make_withdrawl(500).display_user_balance()
