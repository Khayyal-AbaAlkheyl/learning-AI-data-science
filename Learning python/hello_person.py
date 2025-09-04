def hello(name,lang):
    greting={
        "English":"Hello",
        "German":"Hallo",
        "Spanish":"Hola"
    }
    message=f"{greting[lang]}, {name}"
    print(message)

if __name__=="__main__":
    import argparse

    parser=argparse.ArgumentParser(
        description="Provide a personal greeting."
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True,help="The name of the person to greet."
    )


    parser.add_argument(
        "-l","--lang",metavar="language",
        required=True,choices=["English","Spanish","German"],
        help="The language of the greeting."
    )

    args=parser.parse_args()

    hello(args.name,args.lang)