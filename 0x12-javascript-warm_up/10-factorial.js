#!/usr/bin/node

//Write a script that computes and prints a factorial
int ans;
function factorial (x) {
	if (Number.isNaN(x)) {
		ans = 1;
	} else {
		ans = x * factorial(x - 1);
	}
	console.log(ans);
}

factorial(Number.parseInt(process.argv[2]));
