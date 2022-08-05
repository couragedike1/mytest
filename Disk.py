import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)
y = numpy.median(speed)
z = stats.mode(speed)

print("the mean is :" , x)
print("the median is :" , y)
print("the mode is :" , z)



speed = [86,87,88,86,87,85,86]

a = numpy.std(speed)

print("The standard deviation is:", a)

#Percentile

import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(x)


import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("/Users/couragedike/Desktop/Student_performace.csv")


print(df)
