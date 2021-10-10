import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = [21, 22, 23, 4, 5, 6, 77, 8, 9, 10, 31, 32, 33, 34, 35, 36, 37, 18, 49, 50, 100]

#[4, 5, 6, 8, 9, 10, 18, 21, 22, 23, 31, 32, 33, 34, 35, 36, 37, 49, 50, 77, 100]

num_bins = 5
plt.hist(x, num_bins)
plt.show()