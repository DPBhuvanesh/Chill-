import random
import math 
def play():
    user = input("Rock or paper or scissor \n ")
    user=user.lower()
    
    computer = random.choice(['r','p','s'])
    
    if user==computer:
       return (0,user,computer)
    
    if is_win(user,computer):
        return (1,user,computer)
    
    return (-1,user,computer)

def is_win(pi,o):
    if (pi=="r" and o=="s") or (pi=="p" and o=="r") or (pi=="s" and o=="p"):
        return True
    return False 

def best(n):
    pi_wins=0
    o_wins=0
    wins=math.ceil(n/2)
    while pi_wins < wins and o_wins < wins:
        result,user,computer= play()
    
        if result==0:
           print (f"You Both Tie as chosen {user}")
        elif result==1:
            pi_wins+=1
            print (f"You have won as you chose {user} and computer chose {computer}")
        else:
            o_wins+=1
            print (f"You have lost as you chose {user} and computer chose {computer}")
    
    if pi_wins > o_wins :
        print("You have beaten and the best player")
    else :
        print ("You lost , Better Luck Next Time")
        
       
best(3)
