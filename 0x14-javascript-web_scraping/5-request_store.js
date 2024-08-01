#!/usr/bin/node
const url = process.argv[2];
const path = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  } else if (response.statusCode !== 200) {
    console.log('Unexpected status code:', response.statusCode);
    return;
  }
  fs.writeFileSync(path, body, 'utf-8');
});
