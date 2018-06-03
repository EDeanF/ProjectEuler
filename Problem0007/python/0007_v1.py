"""
By listing the first six prime numbers, we can see that the 6th prime is 13

What is the 10,001st prime number?
"""

"""
Brute force method is to build the list of primes until we have 10,001 terms

According to the twin prime conjecture, we may still have to check every odd number for arbitrarily large N

The question is are there quicker tests than checking if the number is divisible by the smaller primes?

We can start by only testing those primes less than sqrt(i)

If we care about size, we should use arrays instead of lists

The number of primes goes as N/ln(N)

"""
#import numpy as np

N = input("Which prime do you wish to find? ")

if N is 1:
    print "P(1) is 2"
elif N is 2:
    print "P(2) is 3"
else:
    Primes=[0]*(N-1)
    Primes[0]=3
    index=1
    number=5
    while index < N-1:
        for j in Primes[0:index]:
            if number % j == 0:
                number+=2
                break
            if j*j > number:
                Primes[index]=number
                number+=2
                index+=1
                break
    print "P({}) is {}".format(N,Primes[N-2])
