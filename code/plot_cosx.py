import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,0.001)
y = np.cos(x)

plt.plot(x,y)
plt.title('Plot of cos(x)')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.grid()

plt.savefig('cosx_plot.png',bbox_inches = "tight")
plt.show()