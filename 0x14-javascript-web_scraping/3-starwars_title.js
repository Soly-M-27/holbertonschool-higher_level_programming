#!/usr/bin/node
/* script that prints the title of a
 * Star Wars movie where the episode
 * number matches a given integer */

const axios = require('axios');
const id = proces.argv[2];
const url = "https://swapi-api.hbtn.io/api/films/";

const res = await axios.get(url, {
	params: {
		'episode_id': id
	}
});

res.data.params['episode_id'];
