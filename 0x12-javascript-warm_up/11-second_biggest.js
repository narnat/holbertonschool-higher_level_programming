#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const arr = process.argv.splice(2);
  let second = Number.MIN_VALUE;
  let max = Number.MIN_VALUE;
  arr.forEach(function (e) {
    if (e > max) {
      second = max;
      max = e;
    } else if (second < e) {
      second = e;
    }
  });
  console.log(second);
}
