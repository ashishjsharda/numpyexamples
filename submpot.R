import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,8,0.1)
y1=np.sin(2*np.pi*t)
y2=np.sin(2*np.pi*t)
plt.subplot(211)
plt.plot(t,y1,'b-.')
plt.subplot(212)
plt.plot(t,y2,'r--')
plt.show()
