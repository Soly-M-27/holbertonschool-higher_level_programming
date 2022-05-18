#!/usr/bin/node
/* script that writes to and prints the content of a file */

const fs = require('fs');

const request = require('request');

const file = process.argv[3];

const content = process.argv[2];

request(content, function (err, res, allcontent) {
  if (err) {
    console.log(err);
  }

  fs.writeFile(file, content, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
