'''Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holde name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality.''' 
class Bankaccount:
  
  def__init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number =account_number 
    self.__account_holder_name=account_holder_name
    self.__account_balance=initial_balance
    
  def deposit(self,amount):
   if amount > 0:
    self.__account_balance+=amount 
#self. __account_balance= self. __account_balance+=amount 
   print ("deposited ₹{} . new balance : {}.".format(amount,self. __account_balance ))
   else:
       print ("invaild deposit amount.")
  def withdraw(self,amount):
    if amount > 0 and amount < =self.__account_balance =amount
#self.__account _balnce=self.__account _balance_amount 
   print ("withdraw ₹{}.New balance: ₹{}".format(account,self.__account_balance ))
else:
   print ("invalid withdrawal amount or insufficient balance")
def display_balance(self):
  print ("account_balance for {}(account #{}:₹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))
#create an instance of the Bankaccount class
account=Bankaccount(account_number="12345678",account_holder_name="Nikitha",initial_balnce=500.0)
#test despoite and withdraw functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(2000.0)
account.display_balance()