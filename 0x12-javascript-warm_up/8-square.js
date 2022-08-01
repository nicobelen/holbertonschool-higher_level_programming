#!/usr/bin/node
const str = 'X';
let i = 0, j = 0;
const arg = parseInt(process.argv[2], 10);
if (!arg) {
  console.log('Missing size');
} else {
  while (i < arg) {
    j = 0;
    while (j < (arg - 1)) {
        process.stdout.write(str);
        j++;
    }
    console.log(str);
    i++;
  }
}
