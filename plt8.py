import numpy as np
import matplotlib.pyplot as plt
a=np.linspace(-5,2,100)
a1=a**3+5*a**2+10
a2=3*a**2+10*a
a3=6*a+10
fig,ax=plt.subplots()
ax.plot(a, a1, color="blue", label="y(x)")
ax.plot(a, a2, color="red", label="y'(x)")
ax.plot(a, a3, color="green", label="y”(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()

