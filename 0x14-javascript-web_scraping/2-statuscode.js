#!/usr/bin/node
// Script that display the status code of a GET request
const request = require('request');
request(process.argv[2], function (error, response, body) {
  error && console.log(error);
  response && console.log('code:', response.statusCode);
});
