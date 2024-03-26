import numpy
from scipy import stats

def mean(array):
    x = numpy.mean(array)
    print(x)

def median(array):
    x = numpy.median(array)
    print(x)

def mode(array):
    x = stats.mode(array)
    print(x)

array = [99,86,87,88,111,86,103,87,94,78,77,85,86]

choice = input("1 for mean, 2 for median, 3 for mode")
if choice == "1":
    mean(array)
if choice == "2":
    median(array)
if choice == "3":
    mode(array)