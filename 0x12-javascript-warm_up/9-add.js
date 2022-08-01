#!/usr/bin/node
let result;
function add (a, b) {
  return (a + b);
}
a = parseInt(process.argv[2], 10);
b = parseInt(process.argv[3], 10);

console.log(add(a, b));
