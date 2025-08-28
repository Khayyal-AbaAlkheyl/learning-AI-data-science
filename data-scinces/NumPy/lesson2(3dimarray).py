import numpy as np
a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a)

#Get a specified element (work outside in )
n=a[0,1,1]
print(n)

#replace
print(a[:,1:])
a[:,1,:]=[[3,3],[4,4]]
print("\n\n")
print(a)



#all zeros
b=np.zeros((3,3))

print(b)


#all ones
b=np.ones((3,3))

print(b)

#any other
b=np.full((3,3),7)

print(b)

#other
c=np.full_like(b,4)
print(c)

#random decimal
m=np.random.rand(3,3)
print(m)

#random integer
k=np.random.randint(-8,7,size=(2,4))
print(k)

#idenity matrix
b=np.identity(3)
print(b)

#repeat an array
r=np.array([[1,2,3]])
r1=np.repeat(r,3,axis=1)
print(r)
print(r1)


#exrcies
e=np.ones((5,5))
e[1:-1,1:-1]=0
e[2,2]=9
print(e)

#copy BE CAREFULL
a=np.array([1,2,3])
b=a
print(a)
print(b)
b[0]=100
print(a)
print(b)
a=np.array([1,2,3])

b=a.copy()
b[0]=100

print(a)
print(b)