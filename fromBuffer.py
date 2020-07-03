import numpy as np
s = b'hello world'
a = np.frombuffer(s, dtype='S1')
print(a)
