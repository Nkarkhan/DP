#!/usr/bin/python

# Input fileName
# FileName format Code and description space delimited
# Sort by Code
# Code should be unique
import pdb
import random
import copy

class Data:
    def __init__(self, data, description):
        self.data = data
        self.description = description
    def __eq__(self, other):
        if self.data != other.data:
            return False;
        if self.description != other.description:
            return False
        return True
    def __ne__ (self, other):
        return not self == other

def insertSorted(sortedList, newElement):
#    pdb.set_trace()
    if len(sortedList) == 0:
        sortedList = [ newElement]
    else:
        l = len(sortedList) - 1
        # Create space in sortedList
        sortedList.append(newElement)
        # Find place in sortedList
        i = l
        while (i >= 0) and (newElement.data < sortedList[i].data):
            sortedList[i+1] = sortedList[i]
            sortedList[i] = newElement
            i = i - 1
    return sortedList

testData = []
testDataSorted = []
sortedOut = []

def genTestData():
    global testData
    n = random.randint(1, 100)
    for i in range(n):
        testData.append(Data(random.randint(1,10000), "Abc"))

def genTestCompData():
    global testData
    global testDataSorted
    testDataSorted = copy.deepcopy(testData)
    testDataSorted.sort(key = lambda x:x.data)

genTestData()
genTestCompData()
soredOut = []
for d in testData:
    sortedOut = insertSorted(sortedOut, d)
if len(testDataSorted) != len(testData):
    pdb.set_trace()
    print "Error"
if len(testDataSorted) != len(sortedOut):
    pdb.set_trace()
    print "Error"
for i in range(len(testDataSorted)):
    if testDataSorted[i] != sortedOut[i]:
        print "Error"
    print ("%d %s \n"%(testDataSorted[i].data, testDataSorted[i].description))

