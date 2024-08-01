#!/usr/bin/node

const request = require('request');
const movie = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';
const util = require('util');
const requestpromise = util.promisify(request);

async function printChar (path) {
  try {
    const response = await requestpromise(path);
    if (response.statusCode !== 200) {
      console.log('Unexpected status code:', response.statusCode);
      return;
    }
    const data = JSON.parse(response.body);
    console.log(data.name);
  } catch (error) {
    console.log(error);
  }
}

async function movieprocess (movieUrl) {
  try {
    const response = await requestpromise(movieUrl);
    if (response.statusCode !== 200) {
      console.log('Unexpected status code:', response.statusCode);
      return;
    }
    const data = JSON.parse(response.body);
    for (const charIndex of data.characters) {
      await printChar(charIndex);
    }
  } catch (error) {
    console.log(error);
  }
}

movieprocess(movie);
