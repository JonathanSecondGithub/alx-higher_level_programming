#!/usr/bin/node

//Write a script that computes and prints a factorial
function factorial (x) {
	if (x === '') {
		return 1;
	}
	x = x - 1;
	return (factorial(x));
}
