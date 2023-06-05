from enum import Enum

saldo = [0]

class menu(Enum):
    
    depositing = 1
    withdrawing = 2
    checking_acct = 3
    exit = 4
    
while True:    

    def prompt():

        opt = int(input("""write: 
                        1 - To deposit
                        2 - Whitdraw
                        3 - Check your balance
                        4 - Exit
                        your number: """))
        return opt

    def info_recieve(opt):
        global saldo
        if opt == menu.depositing.value:
                amount = float(input('insert amount: '))
                saldo[0] += amount
                
        elif opt == menu.withdrawing.value:
                amount = float(input('insert amount to withdraw: '))
                if saldo[0] < amount:
                    print('There´s not enoght balance')
                else:
                    saldo[0] -= amount
                
        elif  opt == menu.checking_acct.value:
                print('current balance: ', saldo[0])   
        
        elif  opt == menu.exit.value:
                print('You selected exit. Bye!')  
                exit()       
        else:
                print('wrong option')   
         
    if __name__=='__main__':
       option = prompt()
       info_recieve(option)
     