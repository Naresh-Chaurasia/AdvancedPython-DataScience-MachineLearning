import matplotlib.pyplot as plt

import numpy as np
x = np.linspace(0, 5, 11)
y = x ** 2

#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html
#FUNCTIONAL

plt.plot(x, y) # 'r' is the color red
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')
plt.show()
