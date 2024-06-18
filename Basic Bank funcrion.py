#Banking Transaction  like Balance,Deposite,Widthdrow

balance=0.00
class bank:
    def __init__(self,balance):
        self.balance_amount=balance
    def balance(self):
        self.check_balance=self.balance_amount
        print("""***********************************""")
        print("Accoun Balance : {}".format(self.check_balance))
        print("""***********************************""")
    def deposite(self):
        self.depos_amount=float(input("Enter Your Amount : "))
        if self.depos_amount>0:
            self.balance_amount+=self.depos_amount
            print("""***********************************""")
            print(f"Deposite Amount : {self.depos_amount}") 
            print("""***********************************""")
        else:
            print("""-----------------------------------""")
            print("Enter tha amount Greater-than of 0")
            print("""------------------------------------""")
    def widthdrow(self):
        self.widthdrow_amount=float(input("Widthdrow Amount : "))
        if self.widthdrow_amount<=self.balance_amount:
            self.balance_amount-=self.widthdrow_amount
            print("""***********************************""")
            print("widthdrow Amount : {}".format(self.widthdrow_amount))
            print("""***********************************""")
        else:
            print("""-----------------------------------""")
            print("Check Your Bank Balance")    
            print("""-----------------------------------""")
Bank=bank(balance)
def main():
 try:
    is_con=True 

    while is_con:
        print("""Welcome To Over Bank
          1.Check Balance
          2.Deposite Amount
          3.widthdrow Amount
          4.Exit
          """) 
        chiose=int(input("Chiose the number(1 to 4) : "))
    
        if chiose==1:
            Bank.balance()
        elif chiose==2:
            Bank.deposite()        
        elif chiose==3:
            Bank.widthdrow()
        elif chiose==4:
           is_con=False
           print("""-------------------------------""") 
           print("""Thank you Enjoy the day 😎🌹🎉""") 
           print("""-------------------------------""")           
        else:
            print("""-------------------------------""")
            print("""Existing Your option's""") 
            print("""-------------------------------""")
 except Exception:
    print("""-------------------------------""")
    print("Your session is close, Here only chiose the Option's")
    print("Try Again") 
    print("""-------------------------------""")          
if __name__=='__main__' :
    main()   
      
