"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?"""

"""
Let's try to solve the problem from 1 to N, instead of 1 to 20

Brute force method:
    Start from N+1
    Check if divisible by 2 to N
    Stop if divisible by all numbers 2 to N

We can also save a lot of time by not checking all numbers greater than N
Instead, just check multiples of N

We definitely can speed up by not checking all numbers 1 to N
For example, if a number is divisble by 20, it is divisible by 2,4,5,10, etc, because these are all factors of 20

So we can first make a list of numbers we need to check, starting from N.
A linked-list is suitable since we only ever need to traverse the list starting from N
On the other hand, a linked-list takes up more space and takes more time to traverse.
The size of the list is bounded by N.
So for large N, it is probably better to use an array. 
We can start with an array of size N and resize it once when we know the final size.


You can probably get the answer from prime factorization

For 1-10
10*9*8*7/2 = 2520
So likely we need to find the prime factorization from which all the 1-N numbers can be made 
i.e.
2^3 * 3^2 * 5 * 7 = 2520

I think the best data structure to store the prime factorization is a hash table
where the hash keys are prime numbers
and the buckets are the number of times that prime appears

However, it is not necessary to store the primes
We can simply keep building the final answer

"""

N=input("What is the last number? ")

Answer=1

def TestPrime(number, prime):
    global TempAnswer
    global Answer
    while number % prime is 0:
        if TempAnswer % prime is 0:
            TempAnswer/=prime
        else:
            Answer*=prime
        number/=prime
    return number

for i in range(N,1,-1) :
    # if Answer is already divisible by i, no further work required
    if Answer % i is 0:
        continue
    
    # store i in local handle, since we will be modifying it
    number=i
    # store Answer in local handle
    TempAnswer=Answer
    
    # if even
    if number % 2 is 0 :
        number = TestPrime(number,2)
    if Answer % number is 0:
        continue

    # continue finding prime factorization of number
    j=3
    while j<=number:
        if number % j is 0:
            number = TestPrime(number,j)
        if Answer % number is 0:
           continue 
        j+=2

print "The answer is", Answer
