class bank:
    def __init__ (self):
        self.pin=''
        self.balance=0
        
        self.menu()
        
    def menu(self):
        a=int(input("Press 1 to set pin\nPress 2 to check balance\nPress 3 to add money\nPress 4 to withdraw money\nPress 5 to exit"))
        
        if a==1:
            self.set_pin()
            
        elif a==2:
            self.check_balance()
            
        elif a==3:
            self.add_money()
            
        elif a==4:
            self.withdraw_money()
            
        elif a==5:
            self.exit()
            
        elif a==6:
            self.check_pin()
            self.menu()
        else:
            # print("you have entered an invalid input")
            pass
            
            
    def set_pin(self):
        self.pin=input("Type your pin")
        print("Pin set successfully")
        self.menu()
            
    def check_balance(self):
        print("your balance is",self.balance)
        self.menu()
    
    def add_money(self):
        add_amount=int(input("please input the amount"))
        self.balance+=add_amount
        print("Amount of ",add_amount," added successfully")
        print("your current balance is - ",self.balance)
        self.menu()
    
    def withdraw_money(self):
        withdraw_amount=int(input("enter the amount"))
        if withdraw_amount>self.balance:
            print("you have insufficient balance")
        else:
            self.balance=self.balance-withdraw_amount
            print("Withdrawal successful")
            print("Your current balance is - ",self.balance)
        self.menu()
        
        
    def check_pin(self):
        print("your pin is - ",self.pin)
    
    def exit(self):
        print("thank you ! \n visit again")
        self.menu()
            
        
        
        
user = bank()