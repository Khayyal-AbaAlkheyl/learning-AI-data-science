from queue import PriorityQueue

import numpy as np
a = np.array([1,2,3,4])

print(a)
a=a+2
print(a)
a=a*2
print(a)
a=a/2
print(a)
a=a-2
print(a)
b=np.array([1,0,1,0])
b=b+a
print(b)
b=b**2
print(b)
b=b**3
print(b)
b=b**4
b=np.sin(b)
print(b)
###Linear algebra
a=np.ones((2,3))
print(a)
b=np.full((3,2),2)
print(b)
m=np.matmul(a,b)
print(m)

c=np.identity(3)
print(np.linalg.det(c))

########stat
stat=np.array([[1,2,3],[7,8,9]])
print(stat)
print(np.min(stat))
print(np.max(stat,axis=1))
print(np.max(stat))
print(np.sum(stat))

##########reorgnizing arrays
before=np.array([[1,2,3],[7,8,9]])
print(before)
after=before.reshape((6,1))
print(after)

######Vertical stack vectors
v1=np.array([1,2,3])
v2=np.array([4,5,6])
v3=np.vstack((v1,v2))
print(v3)
v3=np.vstack((v1,v2,v1,v2))
print(v3)


#Horizontall stack
h1=np.ones((2,4))
h2=np.zeros((2,2))
h3=np.hstack((h1,h2))
print(h3)


####Misc
d=np.genfromtxt('data.txt',delimiter=',')
print(d)
d=d.astype('int32')
print(d)

### Boolean masking and advance indexing\
print (d>5)

print(d[d>5])

## You index with a list in numpy
a=np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,7]])
print((d>5)&(d<10))
print(~(d>5)&(d<10))

a[2:4,0:2]