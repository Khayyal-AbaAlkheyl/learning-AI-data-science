users=['dave','khayyal']
data=['dave',True]
elist=[]

print("dave" in users)

print (users[0])
print (users[-1])

print (users.index('dave'))
print(users[0:])

print(len(users))

users.append("moha")
print(users)
users+=["khaled"]
print(users)

users.extend(['rob','sara'])
print(users)
users.extend(data)
print(users)

users.insert(0,'bob')
users[2:2]=['ahmed','mora']
print(users)
users[1:3]=['hiady','ghsa']
print(users)

users.remove('bob')
print(users)
print(users.pop())
print(users)
del users[0]
print(users)

data.clear()
print (data)
users.sort()
print(users)
nums=[1,5,8,2,4,58,2,3,44]
print(nums)
# nums.sort(reverse=True)
# print(nums)
print(sorted(nums,reverse=True))
print (nums)

numsc=nums.copy()
numsc2=nums[:]
numsc3=list(nums)

print(numsc)
print(numsc2)
numsc3.sort()
print(numsc3)
print(nums)

print(type(nums))

mylist=list(['hi',8,True])
print(type(mylist))
#tupels
mytuple=tuple(('Dave',3,True))
antht=(1,2,4,6,8,8)
print(mytuple)
print(antht)
print(type(antht))
print(type(mytuple))

newlis=list(mytuple)
newlis.append("khayyal")
newtuple=tuple(newlis)
print(newtuple)
(one , tow , *the)=antht
print(one)
print(tow)
print(the)
print(antht.count(8))