#!/usr/bin/node
/* script that writes to and prints the content of a file */

const fs = require('fs');

const readStream = fs.createReadStream(process.argv[2]);

const content = process.argv[3];

fs.writeFile(readStream.toString(), content, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
