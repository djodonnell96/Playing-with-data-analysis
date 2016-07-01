# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 11:08:58 2016

@author: dodonnell
"""

#Algorithm:
#For each item in the data, check against each element in 
#the reference list until a match is found
#Each non-match will be placed in the len(ref)+1th position
#the data is then normalized and returned as percentages 
def findFreq(data, ref):
    #local data
    posCount = [0 for i in len(ref)+1] #Positional count keeps track of how many times data shows up relative to reference list
    #Algorithm above
    for i in range(len(data)):
        refPos = 0 #Referencing begins at 0th index in ref
        found = False #Data assummed to not have found a match yet
        while not found:
            if data[i] == ref[refPos]:
                posCount[refPos] += 1
                found = True
            else:
                refPos += 1
                
    #Normalize data and return
    normalizedFreq = normalize(posCount)
    return normalizedFreq
    
#Utilizes function z(i) = x(i)-minVal/maxVal-minVal to normalize a given dataset
def normalize(data):
    #getting min and max values in the dataset
    normalized = [0 for i in range(len(data))]
    minVal = min(data)
    maxVal = max(data)
    
    #normalization with function z(i) = x(i)-minVal/maxVal-minVal
    for i in range(len(data)):
        numerator = data[i]-minVal
        denominator = maxVal-minVal
        normalized[i] = numerator/denominator
    
    return normalized