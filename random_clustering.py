# -*- coding: utf-8 -*-
from numpy import random as rand
import matplotlib.pyplot as plt

#Data
numPoints = 5555 #self explainatory
maxVal = 10 #max value to use in randint function
data = [0 for i in range(numPoints)] #just filling the data with 0s for now
ref = [] #Reference sheet of possible values

#Initalizing reference table
for i in range(maxVal):
    ref.append(i)
    
#Initalizing graph
plt.ylabel("Value")
plt.xlabel("Index")

#filling data with desired random integers between 0 - maxVal
for i in range(numPoints):
    data[i] = rand.randint(0,maxVal)
    
#Plotting raw data
plt.plot(data, 'ro')

#Begin weird stuff
#Goal here is to find the frequency of each number in the randint function


#Building a distance table
#distanceTable = [[]*numPoints]
#for i in range(numPoints-1):
#    for j in range (numPoints):
#        distanceTable[i,j] = data[i] - data[j]
        
#future: Vector distance as a method of clustering