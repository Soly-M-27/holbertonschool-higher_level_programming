#!/usr/bin/node
if (process.argv.length < 1) {
  console.log('Not a number');
} else if (process.argv.length > 1) {
  if (!parseInt(process.argv[2])) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + parseInt(process.argv[2]));
  }
}
