accounts={"name":"Akosua Aidoo" ,"pin":123,"id":900}
accounts2={"name":"Maxwell","pin":334,"id":500}
accounts3={"name":"Leanne","pin":225,"id":600}
accounts4={"name":"Edwin","pin":5986,"id":2500}
accounts5={"name":"Eric","pin":336,"id":300}
Acc=[] 
Acc.append(accounts)
Acc.append(accounts2)
Acc.append(accounts3)
Acc.append(accounts4)
Acc.append(accounts5)
balance=0

##print(Acc)



def login(accounts):
    
    acc_id=int(input("enter your account id"))
    PIN=int(input('enter your pin'))
    if accounts.get('id')==acc_id and accounts.get("pin")==PIN:
        return("please proceed")
    elif accounts.get('id')!=acc_id and accounts.get("pin")==PIN:
        print("wrong id")
        acc_id=int(input(("re-enter your id")))
    elif accounts.get('id')==acc_id and accounts.get("pin")!=PIN:
        print("invalid pin")
        PIN=int(input("re-enter your pin"))
    else:
        ("you don't have an account in this bank")
        
    
def deposit(accounts):
   
    print("Your initial balance is:{}".format(balance))
    ver_deposit=input("Would you like to deposit?")
    if ver_deposit=="Yes":
        amount_depo=input("Please enter amount")
        new_balance=balance+int(amount_depo)
        print("Your new balance is{}".format(new_balance))
        
    else:
        print("your balance remains unchanged")



def withdrawal(accounts):
    ver_withdraw=input("Would you like to withdraw?")
    if ver_withdraw=="Yes":
        amount=input("please enter the amount")
        print("Your new balance is{}".format(int(amount)+balance))
        
    
        
       



print(login(accounts))
print(deposit(accounts))
print(withdrawal(accounts))
