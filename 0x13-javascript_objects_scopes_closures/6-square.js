#!/usr/bin/node
const square = require('./5-square.js');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let message = '';
        for (let j = 0; j < this.width; j++) {
          message += c;
        }
        console.log(message);
      }
    }
  }
}

module.exports = Square;
