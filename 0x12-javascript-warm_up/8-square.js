#!/usr/bin/node
const size = process.argv[2];

if (parseInt(size)) {
	for (let a = 0; a < size; a++) {
		console.log('X'.repeat(size));
	}
} else {
	console.log('Missing size');
}
