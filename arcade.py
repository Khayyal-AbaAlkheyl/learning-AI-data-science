import sys 
from RPS8 import rps
from guess_number import guessmynmber

def arcade(name="playerone"):
    welcome_back=False
    while True:
        if welcome_back==True:
            print(f"\n{name}, welcome to the arcade menu!")

        playerchoise=input(f"\nplease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nor press \"x\" to exit ")

        if playerchoise not in ["1","2","x"]:
            print(f"\n{name}, please enter 1, 2, or x")
            return arcade()
        

        welcome_back=True

        if playerchoise=="1":
            rock_papper_scissors=rps(name)
            rock_papper_scissors()
        elif playerchoise=="2":
            Guessnum=guessmynmber(name)
            Guessnum()
        else:
           print("\nSee you next time !\n")
           sys.exit(f"Bye {name}!")
        

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
