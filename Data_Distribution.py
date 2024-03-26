import numpy
import matplotlib.pyplot as plt

def randomarray():
    array = numpy.random.uniform(0.0, 5.0, 250)
    return array

array = randomarray()

plt.hist(array)
plt.show()