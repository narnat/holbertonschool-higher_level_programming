#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const res = JSON.parse(body).results;
    let count = 0;
    res.forEach(e => {
      e.characters.forEach(ee => {
        if (ee.includes('/18/')) count++;
      });
    });
    console.log(count);
  }
});
