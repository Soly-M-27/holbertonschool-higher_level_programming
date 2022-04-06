#!/usr/bin/node
exports.esrever = function (list) {
  const nlist = [];
  for (let x = list.length - 1; x >= 0; x--) {
    nlist.push(list[x]);
  }
  return (nlist);
};
