#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.err(err);
  } else if (response.statusCode !== 200) {
    console.log('Unexpected status code:', response.statusCode);
  }
  const data = JSON.parse(body);
  const dict = {};
  for (const i in data) {
    const item = data[i].userId;
    if (dict[item] !== undefined) {
      if (data[i].completed === true) {
        dict[item]++;
      }
    } else {
      dict[item] = 0;
    }
  }
  console.log(dict);
});
