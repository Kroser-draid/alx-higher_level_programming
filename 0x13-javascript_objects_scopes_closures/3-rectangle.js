#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    let message = 'x';
    for (let j = 0; j < (this.width - 1); j++) {
      message += 'x';
    }
    for (let i = 0; i < (this.height - 1); i++) {
      console.log(message);
    }
  }
}

module.exports = Rectangle;
