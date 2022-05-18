#!/usr/bin/node
/* script that gets the contents of a webpage and stores it in a file */

const request = require('request');
const url = process.argv[2];
const content = process.argv[3];
request(url, function (content, err) {
  if (err) {
    console.log(err);
  } else {
    console.log(content);
  }
});
