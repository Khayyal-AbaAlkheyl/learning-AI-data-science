x=1
import numpy as np

x = np.random.rand(3,4,5)
print(x)
print("--------------------------------")
x = x.reshape(-1,1)
print(x.shape)
print(10%3)
a="hello"
print(a*3)
print(7//3)
print("hello"+"lkdc")
a=[1,2,3]
b=a
b[0]=100
print(a)
a=['d','e','f','a']
a.sort()
print(a)

print(np.arange(2,8,3))
print(np.zeros((2,7,8)))
print(np.array([1,2,3]))
a=np.array([1,2,3])
b=np.array([1,5,6])
c=a+b


l=np.array([[1,2,3],[4,5,6 ]])
k=np.array([[7,8,9],[10,11,12]])
h=np.concatenate((l,k),axis=0)
v=np.concatenate((l,k),axis=1)
print(v)
print(h)
print(v.ndim)
print(h)
print(h.prod())
print(h.std())
print(h.mean())
s=np.random.randint(0,2,(4,2))
print(s)
d=np.arange(2,14)
print(d)
array_3, step = np.linspace(0, 10, 3, retstep=True)
print(array_3)
print(step)
print(d.shape)

print(d.reshape((4,3)))