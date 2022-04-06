#!/usr/bin/node
exports.converter = function (base) {
  return tmp => tmp.toString(base);
};
