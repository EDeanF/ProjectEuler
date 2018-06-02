"""
The sum of the squares of the first ten natural numbers is 385
The square of the sum of the first ten natural numbers is 3025
Hence the difference between the sum of the squares and the square of the sum for the first ten natural numbers is 2640

Find the difference between the sum of the squares and the square of the sum of the first one hundred natural numbers
"""

"""
Doing this the brute force method is fairly straight forward...

We can start by remembering that the sum from 1 to N is N*(N+1)/2

Multiplication is the most expensive operation
So we want to try to minimize the number of multiplications,
    but not at the expensive of more operations

In the brute force case, there are 2N+1 operations
    Because we can do the sum instantaneously, we just need 2N to do the sum of the squares

To get the answer directly, we can multiply each number i from 1 to N
     by every other number not equal to i

     sum over i ( sum over j!=i (ij) )

    This has N(N-1)=N^2 -N operations...so much worse
    You could do half the permutations, but that doesn't count for much

So maybe there's a faster way of doing the sum of the squares?

Turns out there is:
N(N+1)(2N+1)/6

N^2 (N+1)^2 /4 - N(N+1)(2N+1)/6
1/4 (N^4+2N^3 +N^2) - 1/6 (2N^3+3N^2+N)
N^4/4 + N^3/6 - N^2/4 - N/6
"""
N = input("What is the largest number? ")

Answer = N**4/4 + N**3/6-N**2/4 -N/6
print "The answer is", Answer
