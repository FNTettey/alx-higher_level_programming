#!/usr/bin/node
module.exports = class Rectangle {
  constructor (width, height) {
    if (typeof (width) === 'number' && typeof (height) === 'number' && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
      this.char = 'X';
    }
  }

  print () {
    for (let i = 0; i < this.height; ++i) {
      let j = 0;

      for (; j < this.width; ++j) {
        process.stdout.write(this.char);
      }

      if (j === this.width) {
        console.log('');
      }
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
