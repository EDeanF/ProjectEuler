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

in retrospect, you have to check through all the possible products anyway, so it is better to take the product of two 3-digit numbers and check if it is a palindrome
"""

import math

