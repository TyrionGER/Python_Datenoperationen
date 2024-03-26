import numpy
import matplotlib.pyplot as plt

def randomarray():
    arrayX = numpy.random.uniform(0.0, 5.0, 250)
    return arrayX

arrayX = randomarray()

plt.hist(arrayX)
plt.show()