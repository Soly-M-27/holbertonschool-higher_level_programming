#!/usr/bin/node
const list = require('./100-data').list;
const map1 = list.map(x => x * 1);
const map2 = list.map((x, idx) => x * idx);

console.log(map1);
console.log(map2);
