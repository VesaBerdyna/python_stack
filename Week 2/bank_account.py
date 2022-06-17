class BankAccount:
   # don't forget to add some default values for these parameters!
   def __init__(self, int_rate, balance=0):
       self.int_rate = int_rate/100
       self.balance = balance 
 
       # your code here! (remember, instance attributes go here)
       # don't worry about user info here; we'll involve the User class soon
 
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
 

