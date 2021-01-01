import numpy as np
import pandas as pd
arr=np.array([1,2,3,4,5])
ser=pd.Series(arr)
print(ser)
#Filter Values
print(ser>3)
