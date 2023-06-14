#!/usr/bin/node

//Write a script that computes and prints a factorial
function factorial (x) {
	if (x === '') {
		ans = 1;
	}
	x = x - 1;
	ans = factorial(x);
	console.log(ans);
}
