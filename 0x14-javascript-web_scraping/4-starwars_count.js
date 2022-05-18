#!/usr/bin/node
/* script that prints the title of a
 * Star Wars movie where the episode
 * number matches a given integer */

const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (res.statusCode === 200) {
    const movies = JSON.parse(body).results;
    for (const id in movies) {
      const moviestars = movies[id].characters;
      for (const star in moviestars) {
        if (moviestars[star].includes('18')) {
			const count = console.count('Wedge Antilles');
        }
      }
    }
	console.log(parseInt(count));
  } else if (err) {
    console.log(err);
  } else {
    console.log('An error occured. Status code: ' + res.statusCode);
  }
});
