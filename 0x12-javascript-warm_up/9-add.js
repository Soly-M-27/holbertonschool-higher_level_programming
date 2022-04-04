#!/usr/bin/node
if (process.argv.length < 2) {
  console.log('NaN');
} else {
  const sum = parseInt(process.argv[2]) + parseInt(process.argv[3]);
  console.log(sum);
}
