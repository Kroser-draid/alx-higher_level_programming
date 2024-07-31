#!/usr/bin/node
const id = process.argv[2];
const path = 'https://swapi-api.alx-tools.com/api/films/' + id + '/';
const request = require('request');

request(path, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log('Unexpected status code:', response.statusCode);
    return;
  }
  const data = JSON.parse(body);
  const title = data.title;
  console.log(title);
});
