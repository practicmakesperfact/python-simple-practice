import numpy
import matplotlib.pyplot as plt

x= numpy.random.normal(5.0,1.0,10000)
plt.hist(x,1000)
plt.show()