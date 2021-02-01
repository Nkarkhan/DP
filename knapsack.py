#!/usr/bin/python

# 0/1 knapsack problem
#  n elements, they all have weights and costs
#  get them into a knapsack with max weight W

testDict = {}
def kp(W, wt, val, n):
    if W == 0 or n == 0:
        return (0, [])
    if wt[n-1] > W:
        # Cant include this element
        ret, elemList =  kp(W, wt, val, n-1)
        return (ret,elemList)
    
    includingElem, elemListInc = kp(W-wt[n-1], wt, val, n-1)
    includingElem =  includingElem + val[n-1]
    elemListInc.append(n-1)
    excludingElem, elemListExcl = kp(W, wt, val, n-1)

    if includingElem >= excludingElem:
        return (includingElem, elemListInc)
    else:
        return (excludingElem, elemListExcl)
    
testDataCost = [ 5,10,1,4,6]
testDataWt = [ 5,10,1,4,6]

n = 5
s = sum(testDataWt)/2
s = 23
print kp(s, testDataWt, testDataCost, 5)
