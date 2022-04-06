#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
      for (let x = 0; x < this.width; x++) {
        console.log(c.repeat(this.height));
      }
    } else {
      for (let x = 0; x < this.width; x++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
