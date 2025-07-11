name ="dave"#global
count=1
def anthother():
    color="green"
    def greetint(name):
        color="blue"
        global count 
        count+=1        
        print(count)
        print(color)
        print(name)
        print(name)

    greetint("khayya")
# def greetint(name):
#     color="blue"
#     print(color)
#     print(name)
#     print(name)

# greetint("hi")

# def anthother():
#     greetint("dave")

anthother()