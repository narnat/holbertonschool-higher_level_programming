#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    if (process.argv[2] === 'http://swapi.co/api/films') {
      const res = JSON.parse(body).results;
      const char = 'https://swapi.co/api/people/18/';
      res.forEach(e => {
        if (e.characters.includes(char)) {
          count++;
        }
      });
    }
    console.log(count);
  }
});
