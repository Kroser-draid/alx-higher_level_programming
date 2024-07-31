#!/usr/bin/node

const request = require('request');
const path = process.argv[2];

request(path, function (err, response, body) {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let occurences = 0;
    for (const filmIndex in films) {
      const filmchars = films[filmIndex].characters;
      for (const charIndex in filmchars) {
        if (filmchars[charIndex].includes('18')) {
          occurences++;
        }
      }
    }
    console.log(occurences);
  } else {
    console.log('Unexpected Status Code:', response.statusCode);
  }
});
