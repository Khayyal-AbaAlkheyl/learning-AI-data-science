#String data type 

#Literal assigment 
first="Khhayl"
last="aba"

# print (type(first))
# print (type(first)==str)
# print(isinstance(first,str))

#constructor function
# pizza=str("pepperoni")
# print (type(pizza))
# print (type(pizza)==str)
# print(isinstance(pizza,str))

#concatination 
fullname=first+" "+last
print(fullname)
fullname+="!"
print(fullname)

#casting a number to a string 

decade = str(1980)
print(type(decade))
print(decade)
statment="I like rock music from the "+decade + "s."
print(statment)


#Multiline strings 
multiline ='''
hey how are you?
are you there ?
               all good?
'''
print(multiline)

#Escaping characters
sentence='I\'m back at work \t Hey\n \n where are are you ?\\'
print(sentence)

#String methods
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good","ok"))
print(multiline)

print(len(multiline))
multiline+="                                   "
multiline="                  "+multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))


#Build a menu 
title ="Menu".upper()
print(title.center(20,"*"))
print("coffee".ljust(16,".")+"1$".rjust(4))
print("Muffine".ljust(16,".")+"2$".rjust(4))
print("chesscakse".ljust(16,".")+"4$".rjust(4))

#Staring index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

#some methodes return boolean data
print(first.startswith("K"))
print(first.endswith("h"))

#boolean data type
myvalue = True 
x=bool(False)
print(type(myvalue))
print(isinstance(myvalue,bool))

#Numric data types
#int
price=100
best_price=int(19)
print(type(price))
print(isinstance(best_price,int))   
#float
gpa=4.50
y=float(3.77)
print(type(gpa))
print(isinstance(y,float)) 
#complex
complex_num=1+2j
print(type(complex_num))
print(complex_num.real)
print(complex_num.imag)

#bulit in functions for numbers
print(abs(-10))  # absolute value
print(round(3.14159))  # round 
print(round(3.14159, 2))  # round to 2 decimal places

import math 
print(math.pi)
print(math.sqrt(16))  # square root
print(math.ceil(4.2))  # ceiling
print(math.floor(4.8))  # floor

#casting a string to a number
zip_code = "12345"
zipnum=int(zip_code)
print(type(zipnum))