#!/usr/bin/node

function send (person, idx) {
  if (idx >= person.length) {
    return;
  }
  request(person[idx], function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      return send(person, ++idx);
    }
  });
}

const request = require('request');
request(`http://swapi.co/api/films/${process.argv[2]}`, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const people = JSON.parse(body).characters;
    send(people, 0);
  }
});
