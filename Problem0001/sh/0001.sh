#!/bin/bash

# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000

read -p 'What is the first factor? ' factor1


read -p 'What is the second factor?' factor2


read -p 'What is the upper bound?' UpperBound

sum=0
multiple=$factor1
while [ $multiple -lt $UpperBound ]
do
	if [ $(( $multiple % $factor2 )) -ne 0 ]
	then
		(( sum+=$multiple ))
	fi
	(( multiple+=$factor1 ))
done

multiple=$factor2

while [ $multiple -lt $UpperBound ]
do
	(( sum+=$multiple ))
	(( multiple+=$factor2 ))
done

echo The answer is $sum
