import numpy as np


print ("hello world")
a =np.array([1,2,3],dtype='int16')
print(a)
b=np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]],dtype='float32')
print(b)


#get dimension
n=a.ndim
print(n)

m=b.ndim

print(m)

#Get Shape

n=a.shape
print(n)

m=b.shape
print(m)


#Get Type
n=a.dtype
print(n)
m=b.dtype
print(m)


#Get size
n=a.itemsize
print(n)
m=b.itemsize
print(m)

#Get total Size
n=a.size
print(n)
m=b.size
print(m)

a1=np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])#should be the same length
print(a1)

#Get a specific row
n=a1[0,:]
print(n)
#Get a specific column
n=a1[:,1]
print(n)


#more fancy way [start index:end index:step size ]
n=a1[0,1:6:2]
print(n)

#change values
a1[1,:]=3
print(a1)
