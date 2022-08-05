import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(x)
print(y)
print(z)



#Pandas Data Frame
import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"], 
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

#Pandas Version
import pandas as pd

print(pd.__version__)


# Pandas Series
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

import pandas as pd 

calories = ["day1", 420, "day2", 380, "day3", 390]

myvar = pd.Series(calories)

print(myvar)


import pandas as pd 

calories = {"day1": 420, "day2": 380, "day3": 390, "day4": 343}

myvar = pd.Series(calories)

print(myvar)


#Data Frame

import pandas as pd 

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
  "fat"     : [56, 56, 90]
}

myvar = pd.DataFrame(data)

print(myvar)


import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)



#Scipy

from scipy import constants 

print(constants.liter)


#Scipy
import scipy

print(scipy.__version__)


#Scipy Tine
from scipy import constants 

print(constants.minute)      
print(constants.hour)
print(constants.day)       
print(constants.week)        
print(constants.year)       
print(constants.Julian_year)


#Scipy

from scipy.optimize import root 
from math import cos 

def eqn(x):
  return x + cos(x)

myroot = root(eqn, 0)

print(myroot.x)

#Plot

import sys
import matplotlib

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dashdot')
plt.title("My Simple Graphy")
plt.grid()
plt.show()


#Graphy Labbeling
import numpy as np
import matplotlib.pyplot as plt



x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid()

plt.show()



