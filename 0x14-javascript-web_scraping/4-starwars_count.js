#!/usr/bin/node

const request = require('request');
request('http://swapi.co/api/people/18', function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).films.length);
  }
});
