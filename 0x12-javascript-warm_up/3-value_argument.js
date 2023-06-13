#!/usr/bin/node

//Write a script that prints the first argument passed to it

#!/usr/bin/node
const arg0 = process.argv[2];

if (arg0 === '') {
	console.log('No argument');
} else {
	console.log(arg0);
}
