#!/usr/bin/node
/* script that writes to and prints the content of a file */

const fs = require('fs');

const file = process.argv[2];

const content = process.argv[3] + '\n';

fs.writeFile(file, content, 'utf8', function(err) {
  if (err) {
    console.log(err);
  }
});
