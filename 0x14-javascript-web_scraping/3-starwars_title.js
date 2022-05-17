#!/usr/bin/node
/* script that prints the title of a
 * Star Wars movie where the episode
 * number matches a given integer */

const axios = require('axios');

const id = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + id;

axios(url, function (res, err) {
  if (err) {
    console.log(err);
  } else {
    console.log(res);
  }
});
