"""
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
factor1=input("What is the first factor?")
while factor1 <=1 :
    print "factor must be greater than 1"
    factor1=input("What is the first factor?")

factor2=input("What is the second factor?")
while factor2 <=1 :
    print "factor must be greater than 1"
    factor2=input("What is the first factor?")

UpperBound=input("What is the upper bound?")
while UpperBound<0:
    print "upper bound must be positive integer"
    UpperBound=input("What is the upper bound?")

def SumDivisibleBy(n) : 
    # sums all multiples of n less than UpperBound
    global UpperBound
    p = (UpperBound-1)/n
    return n*p*(p+1)/2

print "The answer is", SumDivisibleBy(factor1)+SumDivisibleBy(factor2)-SumDivisibleBy(factor1*factor2)
