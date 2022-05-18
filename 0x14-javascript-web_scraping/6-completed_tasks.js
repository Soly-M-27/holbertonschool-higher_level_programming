#!/usr/bin/node
/* script that computes the number of tasks completed by user id */

const request = require('request');

const url = process.argv[2];

request(url, function (err, body) {
	if (err) {
		console.log(err);
	}
	const todo = JSON.parse(body).results;
	const completed = {};
	for (const task in todo) {
		if (task.completed) {
			const id = task.userId;
			completed[id] = (completed[id] + 1 || 1);
		}
	}
	console.log(completed);

});
