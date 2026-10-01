import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,0.001)
y = np.sin(x)

plt.plot(x,y)
plt.title('Plot of sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid()

plt.savefig('sinx_plot.png',bbox_inches = "tight")
plt.show()