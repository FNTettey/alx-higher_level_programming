#!/usr/bin/node

// Creates a Square class that extends Rectangle class

const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c = 'X') {
    super.char = c;
    super.print();
  }
};
