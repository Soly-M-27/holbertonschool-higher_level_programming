#!/usr/bin/node
/* script that reads and prints the content of a file */

const fs = require('fs');

const readStream = fs.createReadStream(process.argv[2], 'utf8');

readStream
  .on('data', function (chunk) {
    console.log(chunk);
  });
