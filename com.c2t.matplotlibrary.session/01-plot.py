import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.sin(x)

print(x)
print(y)

plt.plot(x, y)
#plt.plot(x, y,'r')
plt.show()