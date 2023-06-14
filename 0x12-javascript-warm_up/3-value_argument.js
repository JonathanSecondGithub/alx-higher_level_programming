#!/usr/bin/node

//Write a script that prints the first argument passed to it
const arg0 = process.argv[2];

if (not(arg0)) {
	console.log('No argument');
} else {
	console.log(arg0);
}
