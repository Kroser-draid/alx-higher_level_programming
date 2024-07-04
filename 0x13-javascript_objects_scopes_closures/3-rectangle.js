#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && !Number.isNaN(h) && w > 0 && !Number.isNaN(w)) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = 0; i < (this.height); i++) {
      let message = '';
      for (let j = 0; j < (this.width); j++) {
        message += 'X';
      }
      console.log(message);
    }
  }
};
