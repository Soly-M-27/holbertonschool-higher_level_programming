#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      for (let x = 0; x < this.width; x++) {
        console.log('X'.repeat(this.height));
      }
    } else if (c === 'C') {
      for (let x = 0; x < this.width; x++) {
        console.log('C'.repeat(this.height));
      }
    }
  }
};
