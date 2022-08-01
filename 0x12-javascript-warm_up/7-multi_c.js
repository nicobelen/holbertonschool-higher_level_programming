#!/usr/bin/node
const str = 'C is fun';
let i = 0;
const arg = parseInt(process.argv[2], 10);
if (!arg) {
  console.log('Missing number of occurrences');
} else {
  while (i < arg) {
    console.log(str);
    i++;
  }
}
