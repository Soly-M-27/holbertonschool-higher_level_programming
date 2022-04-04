#!/usr/bin/node
let string = '';
if (process.argv.length <= 2) {
	console.log('Missing size');
} else {
	if (process.argv[2] < 0) {
		return;
	} else {
		for (let x = 0; x < parseInt(process.argv[2]); x++) {
			for (let z = 0; z < parseInt(process.argv[2]); z++) {
				string += 'X';
			}
			if (x === parseInt(process.argv[2]) - 1) {
				string += '';
			} else {
				string += '\n';
			}
		}
	}
	console.log(string);
}
