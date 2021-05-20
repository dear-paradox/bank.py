# bank.py
"""
My first project
using python 
I did this for entertainment
if anyone seen this repo you got any bug in this code , just inform me.....
I complete my python course beginner level 
"""
class Atm:
    def __init__(self):
        self.account = 0
        print("Welcome to Atm")
        print("press 1 to deposite your money ")
        print("press 2 to withdraw your money ")
        print("press 3 to check your balance ")

    def deposite(self):
        slist = ['1']
        number = input("press the number: ")
        while number not in slist:
            print("input number correctly!")
            break

        if number == '1':
            while True:

                amt = float(input("enter your amount to deposite"))
                self.account += amt
                dlist = ['4']
                user = input("press 4 to stop adding your money to account: or continue press any key: ")
                if user in dlist:
                    break
            print("Your deposited amount was: ",amt)

    def withdraw(self):
        alist = ['2']
        number = input("press number '2' to withdraw your money")
        while number not in alist:
            print("input correct number! ")
            break
        
        if number == '2':
            while True:

                amt = float(input("enter your withdraw amount: "))
                if self.account >= amt:
                    
                    self.account -= amt
                    elist = ['5']
                    user = input("press 5 to stop decrease your balance: ")
                    if user == '5':
                        break
                    print("Your withdrawed money was: ",amt)
                    
                else:
                    print("You have insufficeint balance: ")
                    
                        
    def balance(self):
        blist = ['3'] 
        number = input("press '3' view your balance: ")
        while number not in blist:
            print("Input correctly! ")
            break
        if number == '3':
            print("Your cuurent balance of your account: ",self.account)    

    
s = Atm()
s.deposite()
s.withdraw()
s.balance()


        
