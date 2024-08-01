#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode !== 200) {
    console.log('Unexpected status code:', response.statusCode);
  }
  try {
    const data = JSON.parse(body);
    const dict = {};
    for (const item of data) {
      if (!(item.userId in dict)) {
        dict[item.userId] = 0;
      }
      if (item.completed) {
        dict[item.userId]++;
      }
    }
    console.log(dict);
  } catch (parseError) {
    console.log(parseError);
  }
});
