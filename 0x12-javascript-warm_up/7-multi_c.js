#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  const x = process.argv[2];
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
