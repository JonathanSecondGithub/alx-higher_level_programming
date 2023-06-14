#!/usr/bin/node

//Write a script that prints the first argument passed to it
const arg0 = process.argv[2];

if (len(arg0) === 0) {
	console.log('No argument');
} else {
	console.log(arg0);
}
