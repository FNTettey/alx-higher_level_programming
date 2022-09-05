#!/usr/bin/node
const arg = parseInt(process.argv[2]);
let square = '';
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < arg; x++) {
    for (let y = 0; y < arg; y++) {
      square += 'X';
    }
    if (x !== arg - 1) {
      square += '\n';
    }
  }
  console.log(square);
}
