"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?"""

"""
Let's try to solve the problem from 1 to N, instead of 1 to 20

Brute force method:
    Start from N+1
    Check if divisible by 1 to N
    Stop if divisible

We definitely can speed up by not checking all numbers 1 to N
For example, if a number is divisble by 20, it is divisible by 2,4,5,10, etc, because these are all factors of 20

So we can first make a list of numbers we need to check, starting from N.
A linked-list is suitable since we only ever need to traverse the list starting from N
On the other hand, a linked-list takes up more space and takes more time to traverse.
The size of the list is bounded by N.
So for large N, it is probably better to use an array. 
We can start with an array of size N and resize it once when we know the final size.

We can also save a lot of time by not checking all numbers greater than N
Instead, just check multiples of 20

You can probably get the answer from prime factorization

For 1-10
10*9*8*7/2 = 2520
So likely we need to find the prime factorization from which all numbers can be made i.e.
2^4 * 3^3 * 5 * 7 = 2520

We can build the prime factorization using an array again
But this time, there isn't an obvious bound on the size of the array

"""

N=input("What is the last number? ")

# initialize erray 
