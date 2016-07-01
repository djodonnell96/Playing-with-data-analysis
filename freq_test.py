# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 11:08:58 2016

@author: dodonnell
"""

def findFreq(data, ref):
    freq = [0 for i in len(ref)+1]
    #Algorithm:
    #For each item in the data, check against each element in 
    #the reference list until a match is found
    #Each non-match will be placed in the len(ref)+1th position
    #the data is then normalized and returned as percentages
    for i in range(len(data)):
        