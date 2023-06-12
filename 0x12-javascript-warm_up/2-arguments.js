#!/usr/bin/node

//Write a script that prints a message depending of the number of arguments passed

let args = process.argv.length  - 2;

if (args === 0){
	console.log('No argument');
}
else if (args === 1){
	console.log('Argument found');
}
else {
	console.log('Arguments found');
}
