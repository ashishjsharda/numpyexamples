import numpy as np
x=np.array([-1,0,1])
y=np.array([-2,0,2])
X,Y=np.meshgrid(x,y)
print(X)
print(Y)
Z=(X+Y)**2
print(Z)
