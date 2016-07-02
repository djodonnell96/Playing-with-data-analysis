# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 11:08:58 2016

@author: dodonnell
"""

"""
Algorithm:
For each item in the data, check against each element in 
the reference list until a match is found
"""
def findFreq(data_list, ref_list):
    #local data
    refSize = len(ref_list)
    posCount = [0 for i in range(refSize)] #Positional count keeps track of how many times data shows up relative to reference list
    #Algorithm above
    for i in range(len(data_list)):
        refPos = 0 #Referencing begins at 0th index in ref
        found = False #Data assummed to not have found a match yet
        while not found:
            if data_list[i] == ref_list[refPos]:
                posCount[refPos] += 1
                found = True
            else:
                refPos += 1
                
    return posCount
    
"""   
Utilizes function z(i) = x(i)-minVal/maxVal-minVal to normalize a given dataset
"""
def normalize(data):
    #getting min and max values in the dataset
    normalized = [0 for i in range(len(data))]
    minVal = min(data)
    maxVal = max(data)
    denominator = maxVal-minVal #Denominator is a constant for each dataset
    
    #normalization with function z(i) = x(i)-minVal/maxVal-minVal
    for i in range(len(data)):
        numerator = data[i]-minVal
        normalized[i] = numerator/denominator
    
    return normalized