#!/usr/bin/node

const request = require('request');
request(`http://swapi.co/api/films/${process.argv[2]}`, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const people = JSON.parse(body).characters;
    people.forEach(e => {
      request(e, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
