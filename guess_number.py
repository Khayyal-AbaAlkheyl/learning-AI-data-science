import random
import sys 




def guessmynmber(name="KHayyal"):
    player_wins=0
    game_count=0
    winningpersentg=0

    def guessnumber_game():
        nonlocal name
        nonlocal player_wins
        nonlocal game_count
        nonlocal winningpersentg

        playerguess=input(f"\n{name}, guess which number I am thiking of ... 1, 2, or 3\n\n")
        
        
        if playerguess not in ["1","2","3"]: 
            print(f"Please enter  1, 2, or 3")
            return guessnumber_game()
        

        player=int(playerguess)

        computernumber=random.choice("123")

        computer=int(computernumber)

        print(f"\n{name} , you chose  {player}!")
        print(f"I was thiking of  {computer}!\n")
        
        def decide_winner(player,computer):
            nonlocal name
            nonlocal player_wins
            if player==computer:
                player_wins+=1
                return f"{name}, You win🥳"
            else:
                return f"Sorry, {name}. Better luck next time"
        
        game_result=decide_winner(player,computer)
        
        print(game_result)
        
        game_count+=1

        print(f"\ngame count: {game_count}")
        print(f"{name} wins: {player_wins}")
        print(f"Your winning persentage:{player_wins/game_count:.2%}")
        
        print(f"\n\nplay again?, {name}")

        while True:
            playagain=input("\nY for yes \nQ for quit \n\n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break
        
        if playagain.lower()=="y" :
            return guessnumber_game()
        else:
            print("Thank u for playing🥳🥳")
            if __name__=="__main__":
                sys.exit(f"Bye!,{name}!")
            else:
                return

    return guessnumber_game


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

    guess_my_number=guessmynmber(args.name)
    guess_my_number()