#!/usr/bin/node
const argsToConvert = parseInt(process.argv[2]);
if (isNaN(argsToConvert)) {
  console.log('Missing number of occurrences');
} else {
  const x = argsToConvert;
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
