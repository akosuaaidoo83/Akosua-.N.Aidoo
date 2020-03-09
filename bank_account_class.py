import random

class Account:
    def __init__(self,balance):
        
        self.balance=balance
    def Acc_Id(self):
        ac_id=random.randint(99,999)
        print("your account id is {}".format(ac_id))

    def getPin(self):
        pin=input("Enter your pin")
        
        

    def getBalance(self):
        
        print("Your balance is {}".format(self.balance))

    def withdraw(self):
        amount=int(input('To withdraw enter amount here:'))
        min_bal=15000
        if amount<min_bal and amount<self.balance:
            self.balance -= amount
            print('Your new balance is {}.'.format(self.balance))
        else:
            print('Sorry, you cannot withdraw such an amount')
            amount=int(input('Please enter your amount again'))


        
        

    def deposit(self):
        amount=int(input('Enter the amount you want to deposit here'))
        new_bal=self.balance + amount
        print('Your new balance is {}'.format(new_bal))

    







A=Account(600)
A.Acc_Id()
A.getPin()
A.getBalance()
A.withdraw()
A.deposit()
