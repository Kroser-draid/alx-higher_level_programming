#!/usr/bin/node
const api = process.argv[2];
const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);

async function calcoccurences () {
  let occurences = 0;
  const character = 'https://swapi-api.alx-tools.com/api/people/18/';
  for (let i = 1; i < 8; i++) {
    const NewApi = api + '/' + i + '/';
    try {
      const response = await requestPromise(NewApi);
      if (response.statusCode !== 200) {
        console.log('Status Code:', response.statusCode);
        continue;
      }
      const data = JSON.parse(response.body);
      occurences += data.characters.filter(value => value === character).length;
    } catch (error) {
      console.error('Error:', error);
    }
  }
  console.log(occurences);
}
calcoccurences();
