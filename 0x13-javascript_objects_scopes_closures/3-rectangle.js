#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    let message = '';
    for (let j = 0; j < (this.width); j++) {
      message += 'X';
    }
    for (let i = 0; i < (this.height); i++) {
      console.log(message);
    }
  }
}
module.exports = Rectangle;
