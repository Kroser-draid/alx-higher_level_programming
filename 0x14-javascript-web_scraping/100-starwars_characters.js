#!/usr/bin/node

const request = require('request');
const movie = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';


function PrintChar(path) {
  request(path, (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    } else if (response.statusCode !== 200) {
      console.log('Unexpected status code:', response.statusCode);
    }
    const data = JSON.parse(body);
    console.log((data['name']));
  });
}
request(movie, (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    } else if (response.statusCode !== 200) {
      console.log('Unexpected status code:', response.statusCode);
    }
    const data = JSON.parse(body);
    for (charIndex in data.characters) {
      const charLink = data.characters[charIndex];
      PrintChar(charLink);
    }
  });
