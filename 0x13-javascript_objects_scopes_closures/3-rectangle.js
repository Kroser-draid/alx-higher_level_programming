#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && !Number.isNaN(w) && h > 0 && !Number.isNaN(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let message = '';
      for (let j = 0; j < this.width; j++) {
        message += 'X';
      }
      console.log(message);
    }
  }
}

module.exports = Rectangle;
