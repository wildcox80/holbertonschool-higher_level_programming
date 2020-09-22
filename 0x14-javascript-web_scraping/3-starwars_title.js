#!/usr/bin/node
// prints the title of a Star Wars movie
const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  function (err, res, body) {
    if (err) console.log(err);
    console.log(JSON.parse(body).title);
  });
