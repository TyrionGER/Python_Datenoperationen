import numpy

def standard_deviation(array):
    x = numpy.std(array)
    print(x)
def variance(array):
    x = numpy.var(array)
    print(x)

array = [99,86,87,88,111,86,103,87,94,78,77,85,86]

choice = input("1 for standard deviation, 2 for variance")
if choice == "1":
    standard_deviation(array)
if choice == "2":
    variance(array)
