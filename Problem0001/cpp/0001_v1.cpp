// Multiples of 3 and 5
// Problem 1
// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
// Find the sum of all the multiples of 3 or 5 below 1000

#include <iostream>
using namespace std;

int main()
{
	int factor1;
	int factor2;
	int UpperBound;

	cout << "What is the first factor?\n";
	cin >> factor1;
	cout << "What is the second factor?\n";
	cin >> factor2;
	cout << "What is the upper bound?\n";
	cin >> UpperBound;

	int sum = 0;
	int multiple = factor1;

	while (multiple < UpperBound){
		if((multiple%factor2)!=0){
			sum+=multiple;
		}
		multiple+=factor1;
	}

	multiple = factor2;

	while (multiple<UpperBound){
		sum+=multiple;
		multiple+=factor2;
	}
	cout << "The answer is ";
	cout << sum; cout << "\n";
}
