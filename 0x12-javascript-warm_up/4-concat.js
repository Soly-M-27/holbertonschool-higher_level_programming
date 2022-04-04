#!/usr/bin/node
if (process.argv.length < 2) {
  console.log('undefined is undefined');
} else if (process.argv.length > 1) {
  if (process.argv[2] != null && process.argv[3] != null) {
    const a = process.argv[2];
    const b = process.argv[3];
    console.log(a + ' is ' + b);
  } else {
    const a = process.argv[2];
    const b = process.argv[3];
    console.log(a + ' is ' + b);
  }
}
