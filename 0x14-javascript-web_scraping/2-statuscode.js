#!/usr/bin/node
/* Script that displays the status code of a GET request */

const axios = require('axios');

const url = process.argv[2];

axios(url, function (error, res) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
