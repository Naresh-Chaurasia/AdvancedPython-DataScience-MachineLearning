import matplotlib.pyplot as plt

import numpy as np
x = np.linspace(0, 5, 11)
y = x ** 2

# plt.subplot(nrows, ncols, plot_number)
plt.subplot(1,2,1)
plt.plot(x, y, 'r--') # More on color options later
plt.subplot(1,2,2)
plt.plot(y, x, 'g*-');
plt.show()
