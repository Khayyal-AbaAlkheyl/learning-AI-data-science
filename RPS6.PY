import sys 
import random
from enum import Enum

def rps():
    player_wins=0
    python_wins=0
    game_count=0

    def RPS_game():
        nonlocal player_wins
        nonlocal python_wins

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

        print(f"\nYou chose  {str(RPS(player)).replace("RPS.","")}!")
        print(f"Python chose { str(RPS(computer)).replace("RPS.","")}!\n")
        
        def decide_winner(player,computer):
            nonlocal player_wins
            nonlocal python_wins
            if player ==1 and computer ==3:
                player_wins+=1
                return"You win🥳"
            elif player ==2 and computer ==1:
                player_wins+=1
                return"You win🥳"
            elif player ==3 and computer ==2:
                player_wins+=1
                return"You win🥳"
            elif player==computer :
                return"it'a a tie 😒"
            else :
                python_wins+=1
                return"Python win🐍"

        game_result=decide_winner(player,computer)

        print(game_result)
        nonlocal game_count
        game_count+=1


        print(f"\ngame count:{str(game_count)}")
        print(f"\nplayer wins:{str(player_wins)}")
        print(f"\npython wins:{str(python_wins)}")


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
    return RPS_game
play=rps()
play()
