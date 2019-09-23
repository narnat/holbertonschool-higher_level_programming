#!/usr/bin/node

const list = require('./100-data').list;
console.log(`${list}\n${list.map((v, i) => v * i)}`);
