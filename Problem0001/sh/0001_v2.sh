#!/bin/bash

# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000

# define SumDivisibleBy

function SumDivisibleBy() {
	# $1 is the factor whose multiples you would like to sum up to UpperBound
	# $2 is the UpperBound
	local p=$(( ($2-1)/$1 ))
	echo $(( ($p + 1) * $p * $1 / 2 ))
}

read -p 'What is the first factor? ' factor1
read -p 'What is the second factor? ' factor2
read -p 'What is the upper bound? ' UpperBound

sum=0
# bash functions do not return value at the function call

(( sum+=$( SumDivisibleBy $factor1 $UpperBound ) ))
(( sum+=$( SumDivisibleBy $factor2 $UpperBound ) ))
(( sum-=$( SumDivisibleBy $(( factor1*factor2)) $UpperBound ) ))

echo The answer is $sum
