#!/usr/bin/python

# Problem : Minimum Steps To One
# Problem Statement: On a positive integer, you can perform any one of the following 3 steps. 
# 1.) Subtract 1 from it. ( n = n - 1 )  , 
# 2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )  , 
# 3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ). 
# Now the question is, given a positive integer n, find the minimum number of steps that takes n to 1
# eg: 1.)For n = 1 , output: 0       2.) For n = 4 , output: 2  ( 4  /2 = 2  /2 = 1 )    3.)  For n = 7 , output: 3  (  7  -1 = 6   /3 = 2   /2 = 1 )


def minStepsRecur( n ):
    if n == 1:
        return 0
    m1 = -1
    m2 = -1
    m3 = -1
    m1 = 1 + minStepsRecur(n-1)
    if (n%2) == 0:
        m2 = 1 + minStepsRecur(n/2)
    if (n%3) == 0:
        m3 = 1 + minStepsRecur(n/3)
    mList = []
    for x in [m1,m2,m3]:
        if x !=-1:
            mList.append(x)
    return min(mList)

global_memo = {}
def minStepsDp( n ):
    
    try:
        return global_memo[n]
    except:
        m1 = -1
        m2 = -1
        m3 = -1
        m1 = 1 + minStepsDp(n-1)
        if (n%2) == 0:
            m2 = 1 + minStepsDp(n/2)
        if (n%3) == 0:
            m3 = 1 + minStepsDp(n/3)
        mList = []
        for x in [m1,m2,m3]:
            if x !=-1:
                mList.append(x)
        minX = min(mList)
        global_memo[n]=minX
        return minX

def minStepDpTopDown( n ):
    dp = {}
    for i in range(n+1):
        dp[i] = -1
    dp[1] = 0
    for i in range(2, n+1):
        dp[i]=1+dp[i-1]
        if i%2 ==0:
            dp[i]=min(dp[i], dp[i/2]+1)
        if i%3 ==0:
            dp[i]=min(dp[i], dp[i/3]+1)

    return dp[n]

testData = [4, 5, 6, 100, 250]
for t in testData:
    print (" Steps for %d " %t)
    r = minStepsRecur(t) 
    global_memo[1] = 0
    d = minStepsDp(t)
    u = minStepDpTopDown(t)
    if r != d:
        print "Error"
        print r, d
    elif r != u:
        print "Error"
        print r, u
    else:
        print r
