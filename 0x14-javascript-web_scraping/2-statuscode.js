#!/usr/bin/node
/* Script that displays the status code of a GET request */

const request = require('request');

const url = process.argv[2];

request(url, function (error, res) {
	  if (error) {
		  console.log(error);
	  } else {
		  console.log('code: ' + res.statusCode);
	  }
});
