from timeit import timeit
import pandas as pd
#Content 
#1-series
data=[100,200,300,400,500]

s=pd.Series(data,index=['a','b','c','d','e'])
print(s)
print(s.loc['a'])# accessing by label
print(s.iloc[0])# accessing by position
s.loc['b']=656
print(s)
print(s[s>=300])# accessing by condition

cal={"day1":100,"day2":200,"day3":300,"day4":400,"day5":500}
s2=pd.Series(cal)
print(s2)
print(s2.loc['day1'])# accessing by label
print(s2.iloc[0])# accessing by position
s2.loc['day2']=656
print(s2)   
print(s2[s2>=400])
print(s2.index)
num=[1,2,None]# creating a series with None will change the dtype to float
# pandas will automatically convert None to NaN
s3=pd.Series(num)
print(s3) #
students = ['Alice', 'Jack', None]
# And let's convert this to a series
s4=pd.Series(students)#will dtype to object
print(s4)

# NaN is *NOT* equivilent to None and when we try the equality test, the result is False.

# Lets bring in numpy which allows us to generate an NaN value
import numpy as np
# And lets compare it to None
print(np.nan == None)
# It turns out that you actually can't do an equality test of NAN to itself. When you do, 
# the answer is always False. 

np.nan == np.nan# This is because NaN is not a number, so it can't be equal to itself.
# If you want to check if a value is NaN, you can use the numpy function isnan()
print(np.isnan(np.nan))# True

# So keep in mind when you see NaN, it's meaning is similar to None, but it's a 
# numeric value and treated differently for efficiency reasons.

students = [("Alice","Brown"), ("Jack", "White"), ("Molly", "Green")]
s5=pd.Series(students)
print(s5)
print(s5[0])
print(s5[1][1])# accessing second element of first tuple "White"


# Querying `Series`

students_classes = {'Alice': 'Physics',
                   'Jack': 'Chemistry',
                   'Molly': 'English',
                   'Sam': 'History'}
s = pd.Series(students_classes)
print(s)
print(s.index)
print(s['Alice'])# accessing by label
print(s[0])# accessing by position  
print(s.iloc[0])
print(s.loc['Alice'])
# Keep in mind that iloc and loc are not methods, they are attributes. So you don't use 
# parentheses to query them, but square brackets instead, which is called the indexing operator. 
# In Python this calls get or set for an item depending on the context of its use.
class_code = {99: 'Physics',
              100: 'Chemistry',
              101: 'English',
              102: 'History'}
s = pd.Series(class_code)
print(s.iloc[0])#physics not an error 

# Iterating through a Series
grades = pd.Series([90, 80, 70, 60])

total = 0
for grade in grades:
    print(grade)
    total+=grade
print(total/len(grades))

# Here's how we would really write the code using the numpy sum method. First we need to import 
# the numpy module

# Then we just call np.sum and pass in an iterable item. In this case, our panda series.

total = np.sum(grades)
print(total/len(grades))

# Now both of these methods create the same value, but is one actually faster? The Jupyter 
# Notebook has a magic function which can help. 

# First, let's create a big series of random numbers. This is used a lot when demonstrating 
# techniques with Pandas
numbers = pd.Series(np.random.randint(0,1000,10000))# create a series of 10,000 random integers between 0 and 1000
print(numbers.head())
print(len(numbers))   #10000

numbers+=2
print(numbers.head())

# The procedural way of doing this would be to iterate through all of the items in the 
# series and increase the values directly. Pandas does support iterating through a series 
# much like a dictionary, allowing you to unpack values easily.

# We can use the iteritems() function which returns a label and value 

# Here's an example using a Series of a few numbers. 
s = pd.Series([1, 2, 3])

# We could add some new value, maybe a university course
s.loc['History'] = 102
#dttype will be integer because all values are integers
print(s)
students_classes = pd.Series({'Alice': 'Physics',
                   'Jack': 'Chemistry',
                   'Molly': 'English',
                   'Sam': 'History'})
print(students_classes)
kelly_classes = pd.Series(['Philosophy', 'Arts', 'Math'], index=['Kelly', 'Kelly', 'Kelly'])
print(kelly_classes)

# Finally, we can append all of the data in this new Series to the first using the .append()
# function.
all_students_classes = students_classes._append(kelly_classes)

# This creates a series which has our original people in it as well as all of Kelly's courses
print(all_students_classes)

# There are a couple of important considerations when using append. First, Pandas will take 
# the series and try to infer the best data types to use. In this example, everything is a string, 
# so there's no problems here. Second, the append method doesn't actually change the underlying Series
# objects, it instead returns a new series which is made up of the two appended together. This is
# a common pattern in pandas - by default returning a new object instead of modifying in place - and
# one you should come to expect. By printing the original series we can see that that series hasn't
# changed.
print(students_classes)
print(all_students_classes.loc['Kelly'])
sp=pd.Series([12,23,34,45,56])
print(sp[2])