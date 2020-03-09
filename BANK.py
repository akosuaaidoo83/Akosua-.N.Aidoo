import random
 
class Account:
    
    def __init__(self, id, balance = 0):
        self.id = id
        self.balance = balance
        
 
    def getId(self):
        return self.id
 
    def getBalance(self):
        return self.balance
 
 
    def withdraw(self, amount):
        self.balance -= amount
 
    def deposit(self, amount):
        self.balance += amount
 
    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()
def main():

   accounts = []
   for i in range(1000, 9999):
       account = Account(i, 0)
       accounts.append(account)


   while True:
 
       
       id = int(input("\nEnter account pin: "))
 
       
       while id < 1000 or id > 9999:
           id = int(input("\nInvalid Id. Re-enter: "))
 
       
       while True:
 
           
           print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")
 
           
           selection = int(input("\nEnter your selection: "))
 
           
           for acc in accounts:
            
               if acc.getId() == id:
                   accountObj = acc
                   break
                 
           
           if selection == 1:
               
               print(accountObj.getBalance())
 
           
           elif selection == 2:
               
               amt = float(input("\nEnter amount to withdraw: "))
               ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")
 
               if ver_withdraw == "Yes":
                   print("Verify withdraw")
               else:
                   break
 
               if amt < accountObj.getBalance():
                  
                  accountObj.withdraw(amt)
                  
                  print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
               else:
                    print("\nYou're balance is less than withdrawl amount: " + str(accountObj.getBalance()) + " n")
                    print("\nPlease make a deposit.");
 
        
           elif selection == 3:
               
               amt = float(input("\nEnter amount to deposit: "))
               ver_deposit = input("Is this the correct amount, Yes, or No ? " + str(amt) + " ")
 
               if ver_deposit == "Yes":
                  
                  accountObj.deposit(amt);
                
                  print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
               else:
                   break
 
          
 
           
           else:
               print("nThat's an invalid choice.")
 

main()
