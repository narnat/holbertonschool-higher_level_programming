#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const arr = process.argv.splice(2);
  let second = arr[0];
  let max = arr[0];
  arr.forEach(function (e) {
    if (e > max) {
      second = max;
      max = e;
    }
  });
  console.log(second);
}
