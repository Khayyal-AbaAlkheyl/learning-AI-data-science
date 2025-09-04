import sys 
import random
from enum import Enum

def rps(name='playerone'):
    player_wins=0
    python_wins=0
    game_count=0

    def RPS_game():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
    
        
        playerchoise=input(f"{name}, please enter your choise:\n1 for rock\n2 for paper\n3 for scissors\n")
        
        if playerchoise not in ["1","2","3"]:
            print(f"{name}, please enter 1,2,or 3")
            return RPS_game()
        
        player=int(playerchoise)

    
        computerchoise=random.choice("123")

        computer=int(computerchoise)

        print(f"\n{name} , you chose  {str(RPS(player)).replace('RPS.','')}!")
        print(f"Python chose { str(RPS(computer)).replace('RPS.','')}!\n")
        
        def decide_winner(player,computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player ==1 and computer ==3:
                player_wins+=1
                return f"{name}, You win🥳"
            elif player ==2 and computer ==1:
                player_wins+=1
                return f"{name}, You win🥳"
            elif player ==3 and computer ==2:
                player_wins+=1
                return f"{name}, You win🥳"
            elif player==computer :
                return"it'a a tie 😒"
            else :
                python_wins+=1
                return f"Python win🐍\nSorry, {name}.."

        game_result=decide_winner(player,computer)

        print(game_result)
        nonlocal game_count
        game_count+=1


        print(f"\ngame count: {game_count}")
        print(f"{name} wins: {player_wins}")
        print(f"\npython wins: {python_wins}")


        print(f"\n\nplay again?, {name}")

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
            sys.exit(f"Bye!,{name}!")

    return RPS_game


if __name__=="__main__":
    import argparse

    parser=argparse.ArgumentParser(
        description="Provide a personalized game experince."
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True,help="The name of the person playing the game."
    )

    args=parser.parse_args()

    rock_paper_scissors=rps(args.name)
    rock_paper_scissors()