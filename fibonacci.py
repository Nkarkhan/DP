#!/usr/bin/python

# Fibonacci 
# f(0) = 1, f(1) = 1, f(2) = f(0) + f(1), f(n) = f(n-1) + f(n-2)
# Solve by recursion and dynamic programming

from timeit import default_timer as timer
def fibRecur( n ):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f = fibRecur(n-1) + fibRecur(n-2)
    return f

def fibDpMemo ( n ):
    try:
        return memo[n]
    except:
        m1 = fibDpMemo(n-1)
        memo[n-1] = m1
        m2 = fibDpMemo(n-2)
        memo[n-2] = m2
        return m1 + m2

def fibDpTopDown( n ):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fnMinus1 = 1
    fnMinus2 = 0
    for i in range(2, n+1):
        fn = fnMinus1 + fnMinus2
        fnMinus2 = fnMinus1
        fnMinus1 = fn
    return fn

testData = [ 0,1,2,3,4, 20, 30, 35, 40]
memo = {}
for t in testData:
    start = timer()
    r = fibRecur(t)
    end = timer()
    rTime = end-start
    memo[0] = 0
    memo[1] = 1
    memo[2] = 1
    start = timer()
    m = fibDpMemo(t)
    end = timer()
    mTime= end - start
    start = timer()
    td = fibDpTopDown(t)
    end = timer()
    tdTime = end - start
    if (r != m or m != td) or (rTime > 5.0) :
        print("%d Fibonacci number by recursion is %d in time %f"%(t, r, rTime))        
        print("%d Fibonacci number by memo dp is %d in time %f"%(t, m, mTime))
        print("%d Fibonacci number by memo dp is %d in time %f"%(t, td, tdTime))
