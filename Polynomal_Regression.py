import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


xArray = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
yArray = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

mymodel = numpy.poly1d(numpy.polyfit(xArray, yArray, 3))

myline = numpy.linspace(1, 22, 100)


print(r2_score(yArray, mymodel(xArray)))

prediction = mymodel(17)
print(prediction)

plt.scatter(xArray, yArray)
plt.plot(myline, mymodel(myline))
plt.show()