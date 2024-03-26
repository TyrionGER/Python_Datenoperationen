import matplotlib.pyplot as plt
import scipy.stats as stats
import Scatter_Plot

xArray = Scatter_Plot.randomarray(100)
yArray = Scatter_Plot.randomarray(100)

slope, intercept, r_value, p_value, std_err = stats.linregress(xArray, yArray)

print(r_value) #Relationship coefficient

def myfunc(array):
    return slope * array + intercept

mymodel = list(map(myfunc, xArray))

plt.scatter(xArray, yArray)
plt.plot(xArray, mymodel)
plt.show()
