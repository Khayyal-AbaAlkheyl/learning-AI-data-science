import sys 
import random
from enum import Enum
def RPS_game():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
   
    
    playerchoise=input("Enter your choise:\n1 for rock\n2 for paper\n3 for scissors\n")
    
    if playerchoise not in ["1","2","3"]:
        print("You must enter 1,2,or 3")
        return RPS_game()
    
    player=int(playerchoise)

   
    computerchoise=random.choice("123")

    computer=int(computerchoise)

    print("")
    print("You chose " + str(RPS(player)).replace("RPS.","")+"!")
    print("Python chose " + str(RPS(computer)).replace("RPS.","")+"!")
    print("")

    if player ==1 and computer ==3:
        print("You win🥳")
    elif player ==2 and computer ==1:
        print("You win🥳")
    elif player ==3 and computer ==2:
        print("You win🥳")
    elif player==computer :
        print("it'a a tie 😒")
    else :
        print("Python win🐍")
    print("\n\nplay again?")

    while True:
        playagain=input("\nY for yes \nQ for quit \n\n")
        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break
    
    if playagain.lower()=="y" :
       return RPS_game()
    else:
        print("Thank u for playing🥳🥳")
        sys.exit("Bye!")
RPS_game()

