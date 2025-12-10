import sys 
import random
from enum import Enum
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
playerchoise=input("Enter your choise:\n1 for rock\n2 for paper\n3 for scissors\n")
player=int(playerchoise)
if player > 3 or player < 1 :
    sys.exit("You must enter 1,2,or 3")
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
