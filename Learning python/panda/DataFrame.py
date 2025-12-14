import pandas as pd
import numpy as np  
data={"Name":["Tom","nick","krish","jack"],
      "Age":[20,34,43,23]}    

df=pd.DataFrame(data,index=["e1","e2","e3","e4"])
print(df)   
print(df.loc["e2"])# accessing row by label])
print(df.iloc[2])# accessing row by position
#new column
df["jop"]=['1',2,3,5]
print(df)
#add a new row
new_rows=pd.DataFrame([{"Name":"Sara","Age":25,"jop":4}],index=["e5"])
df=pd.concat([df,new_rows])
print(df)
new_rows=pd.DataFrame([
    {"Name":"gdfg","Age":25,"jop":4},
    {"Name":"Lina","Age":30,"jop":6}
                       ],index=["e6","e7"])
df=pd.concat([df,new_rows])
print(df)
print(df.T)# transpose
print(df[df["Age"]>30])# accessing by condition
print(df.index)
print(df.T.loc["Age"])
print(df.loc[:,["Name","jop"]])#print without a loc here is an error
print(df.drop("e1"))#it dosen't change the original
print(df)
# Drop has two interesting optional parameters. The first is called inplace, and if it's 
# set to true, the DataFrame will be updated in place, instead of a copy being returned. 
# The second parameter is the axes, which should be dropped. By default, this value is 0, 
# indicating the row axis. But you could change it to 1 if you want to drop a column.

# For example, lets make a copy of a DataFrame using .copy()
copy_df = df.copy()
# Now lets drop the name column in this copy
copy_df.drop("Name", inplace=True, axis=1)
print(copy_df)

# There is a second way to drop a column, and that's directly through the use of the indexing 
# operator, using the del keyword. This way of dropping data, however, takes immediate effect 
# on the DataFrame and does not return a view.
del copy_df['Age']
print(copy_df)

df["nonecloumn"]=None
print(df)

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj1 = pd.Series(sdata)
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj2 = pd.Series(sdata, index=states)
obj3 = pd.isnull(obj2)
print(obj1)
print(obj2)
print(obj3)
s1 = pd.Series({1: 'Alice', 2: 'Jack', 3: 'Molly'})
s2 = pd.Series({'Alice': 1, 'Jack': 2, 'Molly': 3})



print(s2[1])

print(s1.loc[1])



print(s2.iloc[1])
print(s1.iloc[1])