def hello():
    print("Hello world!")

hello()

def sum(num1,num2):
    print(num1+num2)


def sum1(num1,num2=6):
    if(type(num1) is not int or type(num2) is not int ):
     return
    return num1+num2

sum(1,2)
total=sum1(1)
print(total)

def multiple_items(*args):
   print(args)
   print(type(args))

multiple_items("khayyal","dgs","hhu")

def multni(**kwargs):
   print(kwargs)
   print(type(kwargs))

multni(first="khayyal",last="hhu")
