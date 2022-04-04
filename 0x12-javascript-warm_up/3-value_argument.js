#!/usr/bin/node
if (process.argv[1]) {
  if (!process.argv[2]) {
    console.log('No Argument');
  } else {
    const arg = process.argv[2];
    console.log(arg);
  }
}
