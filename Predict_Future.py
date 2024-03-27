from matplotlib import pyplot as plt
from scipy import stats


xArray = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
yArray = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r_value, p_value, std_err = stats.linregress(xArray, yArray)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, xArray))

plt.scatter(xArray, yArray)
plt.plot(xArray, mymodel)
plt.show()

predicition = myfunc(10)

print (predicition)
