#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else if (process.argv.length > 2) {
  const arr = [];
  for (let idx = 2; idx < process.argv.length; idx++) {
    arr.push(parseInt(process.argv[idx]));
  }
  arr.sort(function (a, b) { return a - b; });
  console.log(arr[arr.length - 2]);
}
