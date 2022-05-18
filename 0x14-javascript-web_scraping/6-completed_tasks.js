#!/usr/bin/node
/* script that computes the number of tasks completed by user id */

const request = require('request');

const url = process.argv[2];

request(url, function (res, err, body) {
  if (err) {
    console.error(err);
  }
  const todo = JSON.parse(body);
  const completed = {};
  for (const task in todo) {
    if (task.completed) {
      const id = task.userId;
      completed[id] = (completed[id] + 1 || 1);
    }
  }
  console.log(completed);
});
