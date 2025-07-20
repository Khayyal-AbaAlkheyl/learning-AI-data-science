class JustNotCoolError(Exception):
    pass


x=2
try:
   raise JustNotCoolError ("This isn't cool, man")
   # print(x/0)
   if not type(x) is str:
      raise TypeError("Only string are allowed")
except NameError:
    print("Nameerror means that is something is undefined")
except ZeroDivisionError:
    print("Please do not divide by 0.")
except Exception as error:
    print(error)
else:
    print("Np errors!")
finally:
    print("I'am going to print with or without an error")