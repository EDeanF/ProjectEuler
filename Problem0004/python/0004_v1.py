"""
A palindromic number reads the same both ways. The largest palidrome made from the product of two 2-digit numbers is 9009 = 91*99

Find the largest palindrome made from the product of two 3-digit numbers
"""

"""
the product is bound by 999*999 = 998001 and 100*100 = 10000
so the palindrome is bound by 997799 and 10001

there are two possible brute force approaches
    (1) make a palindrome and check if it is the product of two 3-digit numbers
    (2) take the product of two 3-digit numbers and check if it is a palindrome

checking if a number is a palindrome is cheap compared to looking for factors

there are 8*10*10 + 9*10*10 = 1700 possible palindromes to check

there are 0.5*(9*10*10)^2 = 405000 possible products

If we think how to solve the problem for two n-digit numbers,
going through all the possible palindromes should scale better

abc * DEF = (100a + 10b + c)*(100D + 10E +F)
abc * DEF = aD 10^4 + (aE + bD) 10^3 + (aF + bE + cF) 10^2 + (bF + cF) 10 + cF
"""

import math

def MakePalindrome(d1,d2,d3) :
    return d1*100000 + d2*10000 + d3*1000 + d3*100 + d2*10 + d1

def IsProduct(n) :
    # checks if n is the product of two three digit numbers
    factor1=100
    factor2=100
    while factor1<min(math.sqrt(n),999) :
        if n % factor1 is 0 :
            factor2 = n/factor1
            if factor2 in range(100,999) :
                return True
        factor1+=1
    return False

digit1=9
digit2=9
digit3=7

while digit1>0 :
    while digit2>=0 :
        while digit3>=0 :
            Palindrome=MakePalindrome(digit1,digit2,digit3)
            if IsProduct(Palindrome) :
                print "The answer is", Palindrome
                exit()
            digit3-=1
        digit2-=1
        digit3=9
    digit1-=1
    digit2=9


