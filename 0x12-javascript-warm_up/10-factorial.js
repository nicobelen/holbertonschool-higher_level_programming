#!/usr/bin/node
const num = parseInt(process.argv[2], 10);
function factorialize (num) {
  if (num === 0 || !num) {
    return 1;
  } else {
    return (num * factorialize(num - 1));
  }
}
console.log(factorialize(num));
