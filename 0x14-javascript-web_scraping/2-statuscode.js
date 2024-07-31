#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('Error:', error.message);
    return;
  }

  if (!response) {
    console.error('No response received');
    return;
  }

  console.log('code:', response.statusCode);
});
