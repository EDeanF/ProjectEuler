"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

import math

n=600851475143

def IsPrime(n) :
    if n % 2 is 0 :
        return False
    else :
        i = 3
        while i < math.sqrt(n) :
            if n % i is 0 :
                return False
            i+=2
        return True

LargestPrimeFactor=1

# factors always come in pairs
Factor1=2
Factor2=1

while Factor1 < math.sqrt(n):
    if n % Factor1 is 0 :
        Factor2= n/Factor1
        if IsPrime(Factor2) :
            LargestPrimeFactor = Factor2
            break
        elif IsPrime(Factor1) :
            LargestPrimeFactor = Factor1

    Factor1+=1

print "The Largest Prime Factor is " , LargestPrimeFactor
