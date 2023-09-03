import random
name=input("Enter your name:")
n=int(input("Enter number of rounds:"))


def game():
    rounds=1
    winner=None
    while rounds<=n:
        #rounds = rounds+1  
        print(f"Round :{rounds}")
     
        print("Computer Turn: Snake(s) Water(w) or Gun(g)")
        randomnumber= random.randint(1,3)
        if randomnumber==1:
            computer='s'
        elif randomnumber==2:
            computer='g'
        elif randomnumber==3:
            computer='w'

        player=input("It's your turn Choose any one:Snake(s) Water(w) or Gun(g)")
        
        if computer==player:
            winner=None
        elif computer=='s':
            if player=='w':
                winner=False
            elif player=='g':
              winner=True
        elif computer=='w':
            if player=='g':
                winner=False
            elif player=='s':
                winner=True
        elif computer=='g':
            if player=='s':
                winner=False
            elif player=='w':
                winner=True  
        rounds=rounds+1
    return winner

a = game()        
if a==None:
    print("The game is tie!")
elif a:
    print(f"{name} Win!")
else:
    print(f"{name} Loose!")        



