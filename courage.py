
#Arrarys#
cars = ["Ford", "Volvo", "BMW", "Benez"]

n = cars[3]
cars.append("Honda")
cars.remove("Volvo")

print(cars)


class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)


#Learn Classes#

class Person:
  def __init__(self, name, age, sex):
    self.name = name
    self.age = age
    self.sex = sex

p1 = Person("John", 36, "Male")

print(p1.name)
print(p1.age)
print(p1.sex)


class Person:
  def __init__(self, name, age, sex):
    self.name = name
    self.age = age
    self.sex = sex

  def myfunc(self):
    print("Hello my name is " + self.name + " I am a " + self.sex)

p1 = Person("John", 36, "male")
p1.myfunc()

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


import numpy as np
arr = np.array([1, 2, 3, 4, 5])

print(arr)


import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)

#Date

import datetime

x = datetime.datetime.now()

print(x)
print(x)


import datetime

x = datetime.datetime(2020, 5, 17)

print(x)


import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


import datetime

x = datetime.datetime.now()

print(x.strftime("%%"))

#Maths in Python

x = min(1, 5, 10, 20, 60, 90, 100)
y = max(1, 5, 10, 25, 50, 80, 100)

print(x)
print(y)

#Power Function In Maths
x = pow(9, 3)

print(x)


import math

x = math.sqrt(64)

print(x)

#Import math library
import math

#Round a number upward to its nearest integer
x = math.ceil(4.5)

#Round a number downward to its nearest integer
n = math.floor(4.5)

print(x)
print(n)

#Pi in Maths

import math

x = math.pi

print(x)


#importing JSON
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(y["name"])
print(y["city"])


import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)



import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


import numpy as np

print(np.__version__)


import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("in", txt)
print(x)


import re

txt = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Spain", txt)
print(x)

#if else statement

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")



#Carmeal Case Import

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))


#Import Matplotlib

import matplotlib

print(matplotlib.__version__)


#The try block does not raise any errors, so the else block is executed:

try:
  print(x)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


#Input Code 


username = input("Enter username:")
password = input("Enter password:")
print("Username is correct:" + username)
print("Paasword is correct:" + password)



#My order

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))



#Import Matplotlib

import matplotlib

print(matplotlib.__version__)


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 5])
ypoints = np.array([0, 100])

plt.plot(xpoints, ypoints)
plt.show()


#indexing 2 dimensional Array

import numpy as np

x = np.array([[1,2,3,4,5,7], [6,7,8,9,10,17]])

print('2nd element on 1st row: ', x[1, 5])


from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y) 






























