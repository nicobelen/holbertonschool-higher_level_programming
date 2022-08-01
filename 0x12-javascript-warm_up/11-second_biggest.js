#!/usr/bin/node
const arg = process.argv;
const length = process.argv.length;
let i = 2;
let result = 0;
let second = 0;
if (!arg || length < 2) {
  console.log(second);
} else {
  while (i < length && arg[i + 1]) {
    if (parseInt(arg[i], 10) > parseInt(arg[i + 1], 10)) {
      if (result < arg[i]) {
        result = arg[i];
      }
    } else {
      if (result < parseInt(arg[i + 1], 10)) {
        result = arg[i + 1];
      }
    }
    i++;
  }
  i = 2;
  while (i < length) {
    if (arg[i] > second && arg[i] < result) {
      second = arg[i];
    }
    i++;
  }
  console.log(second);
}
