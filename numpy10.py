import numpy as np
a=np.arange(0,60,5)
a=a.reshape(3,4)
print(a)
print('Transpose of a is',a.T)
b=a.T
c=b.copy(order='C')
print("Value of c is ---------------------")
print(c)
for x in np.nditer(c):
    print(x)
