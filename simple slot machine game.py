import random
# def sub(wallet,bet):
#     wallet-=bet
def slot():
    items=['🍇','🍌','🍊','🏆']
    result=[]
    for _ in range(3):
       result.append(random.choice(items)) 
    return result   
def print_result(res):
    print(str(" | ".join(res)))
def pay_multple(final_res,bet):
    if final_res[0]==final_res[1]==final_res[2]:
        if final_res[1]=='🍇':
            return bet *3
        elif final_res[1]=='🍌':
            return bet *6
        elif final_res[1] =='🍊':
            return bet * 15
        elif final_res[1]=='🏆':
            return bet * 19
    return 0     
def main():    
    print("Welcome To Slot Machine")
    print("************************" )
    print("""🍇   🍌  🍊  🏆""")
    print("************************")
    wallet=100
    
    while True:
        print("Your Current Balance : {}".format(wallet))
        
        bet=(input("Enter Your Beting Amount : "))
        
        if not bet.isdigit():
            print("Enter Your  Valied Number")
            continue
             
        bet=int(bet)
        
        if bet>wallet:
            print("Check Your Current Balance")
            continue
        elif bet<=0:
            print("Plice Enter Geaterthan (>) 0")
            continue
        wallet-=bet
        print("**************************")
        print(f"Youe Beting Amount {bet}")
        res=slot()
        # print(res)
        print_result(res)
        
        res_2=pay_multple(res,bet)
        win_amount=0
        win_amount+=res_2
        if res_2>0:
            print(f"Your Win : {res_2}")
            wallet+=res_2
            print("***********************")
        else:
            print("You lose This Round")   
            print("***********************") 
        confom=input("Continue Next Round (Y/N) : ").upper().strip()
        
        if confom in "Y":
            continue              
        else:
            print("Game Over!")
            print(f"Total Wining  Ammount : {win_amount}")     
            print(f"Your Current Balance {wallet}")  
        break
if __name__=='__main__':
    main()
