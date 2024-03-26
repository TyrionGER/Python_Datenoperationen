import numpy
import matplotlib.pyplot as plt

def randomarray(x):
    array = numpy.random.normal(0.0, 5.0, x)
    return array

xArray = randomarray(1000)
yArray = randomarray(1000)

plt.scatter(xArray, yArray)
plt.show()