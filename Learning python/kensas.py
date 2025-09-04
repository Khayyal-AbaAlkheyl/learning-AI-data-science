from random import choice

capital="Buridah"

bird="dkhl"

flower="athel"

song="damazk"

def randomfunfact():
    funfact=[
        "buridah is godd",
        "hail is better",
        "alriadh best",
        "kidding its the best"
    ]

    index=choice("0123")

    print(funfact[int(index)])

if __name__=="__main__":
    randomfunfact()