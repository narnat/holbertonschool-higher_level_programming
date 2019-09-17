#!/usr/bin/node
function fact (a) {
  if (a === 0 || a === 1 || isNaN(a)) {
    return (1);
  }
  return (fact(a - 1) * a);
}
console.log(fact(parseInt(process.argv[2])));
