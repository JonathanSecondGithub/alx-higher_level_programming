#!/usr/bin/node

//Write a script that computes and prints a factorial
function factorial (x) {
	if (x === '') {
		ans = 1;
	} else {
		ans = ans * factorial(x - 1);
	}
	console.log(ans);
}
