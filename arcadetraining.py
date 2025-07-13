import sys 
from RPS8 import rps
from guess_number import guessmynmber

def arcade(name="playerone"):
    print(f"\n{name}, welcome to the arcade!")
    def arcadeGame():
        choise=input(f"\nplease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nor press \"x\" to exit ")

        
        def desison(choise):
            if choise == "1":
                rps()
            elif choise =="2" :
                guessmynmber()
            elif choise=="x":
                exit(f"\nYou have exited the arcade nice to have you")
            else:
                return arcadeGame()
    return arcadeGame()


if __name__=="__main__":
    import argparse

    parser=argparse.ArgumentParser(
        description="Provide a personal greeting."
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True,help="The name of the person to greet."
    )

    args=parser.parse_args()


    arcade_=arcade(args.name)

    arcade_()
