"""
Rock : Paper (Paper)
Paper : Scissors (Scissors)
Rock : Scissors (Rock)
"""

import random
import time
from colorama import Fore,Style,Back,init

c=0
u=0


def inputHandler(inpt):
    inpt=inpt.lower()
    passOutput="rock paper scissors"
    r,p,s=passOutput.split()
    rval,pval,sval=0,0,0
    inptList=list(inpt)
    pList=[list(r),list(p),list(s)]
    for k in pList:
        i=0
        for l in k:
            try:
                if(l == inptList[i]):
                    if(k == list(r)):
                        rval+=1
                    elif(k == list(p)):
                        pval+=1
                    elif(k == list(s)):
                        sval+=1
                i+=1
            except IndexError:
                break
    if(rval == pval and pval == sval):
        print(Back.WHITE)
        print("___Invalid input___")
        time.sleep(0.5)
        print(Back.RESET)
        return -1
    else:
        w=max(rval,pval,sval)
        if(w== rval):
            return r
        elif(w== pval):
            return p
        elif(w== sval):
            return s
        
            
    
# computer's choice
def computers_choice():
    return (random.choice([-1,0,1]))

def win_dec(user,computer):
    if (user == computer):
        print("\nIt's a tie\n")
    else:
        if ((user == 0 and computer == -1) or (user == 1 and computer == 0) or  (user == -1 and computer == 1)):
            global u
            u+=1
            col()
            print("User Wins !")
        else:
            global c
            c+=1
            col()
            print("Computer Wins!")
            
def col():
    global u
    global c
    diff = u-c
    if(diff == 0):
        print(Fore.RESET)
    if(diff == 1):
        print(Fore.MAGENTA)
    if(diff == 2):
        print(Fore.LIGHTMAGENTA_EX)
    if(diff >= 3):
        print(Fore.BLUE)
    if(diff == -1):
        print(Fore.YELLOW)
    if(diff == -2):
        print(Fore.LIGHTRED_EX)
    if(diff <= -3):
        print(Fore.RED)
    





rps ={"rock":-1,"paper":0,"scissors":1}
revRPS={-1:"rock",0:"paper",1:"scissors"}
user = ""
print("Enter Rock,Paper,Scissors(wrong input can be auto corrected to some extent )")

while(True):
    
    print("Enter '0' to exit")
    print(f"Computer: {c} ")
    print(f"User: {u}")

    uinput = input("Your choice: ")
    if ((uinput) == "0" ):
        print(Fore.RESET,end="")
        print("___EXIT___")
        break
    user = inputHandler(uinput)
    if(user == -1):
        continue
    computer = computers_choice()
    print(f"Computer's choice: {revRPS[computer]}")
    try:
        win_dec(rps[user],computer)
    except KeyError:
        break
    

