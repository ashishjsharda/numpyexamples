import numpy as np
import  pandas as pd
a=np.array([5,2,19,12])
s=pd.Series(a)
print(s[s>8])
print(s/2)
print(np.log(s))
