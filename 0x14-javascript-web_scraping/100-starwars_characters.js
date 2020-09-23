#!/usr/bin/env node
// retrieves all character names in SW film
const request = require('request');
const FILM_URL = `http://swapi.co/api/films/${process.argv[2]}`;
request(FILM_URL, function (err, res, body) {
  if (err) return console.log(err);

  body.characters.forEach(e => {
    request(e, { json: true }, (err, res, body) => {
      if (err) return console.log(err);

      console.log(body.name);
    });
  });
});
