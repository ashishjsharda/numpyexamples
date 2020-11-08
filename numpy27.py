import numpy as np
f=lambda m,n:n+10*m
A=np.fromfunction(f,(6,6),dtype=int)
print(A)
print(A[:,0]) #print first column
print(A[0,:]) #print first row

