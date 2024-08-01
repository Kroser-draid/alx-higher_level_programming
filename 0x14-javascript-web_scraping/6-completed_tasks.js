#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode !== 200) {
    console.log('Unexpected status code:', response.statusCode);
  }
  const data = JSON.parse(body);
  const dict = {};
  for (const i in data) {
    const item = data[i].userId;
    if (dict[item] === undefined && data[i].completed === true) {
      dict[item] = 1;
    } else if (dict[item] !== undefined && data[i].completed === true) {
      dict[item]++;
    } else if (dict[item] === undefined && data[i].completed === false) {
      dict[item] = 0;
    }
  }
  console.log(dict);
});
