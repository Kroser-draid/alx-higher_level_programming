#!/usr/bin/node
const arg = process.argv[2];
const fs = require('fs');

try {
  const data = fs.readFileSync(arg, 'utf-8');
  console.log(data);
} catch (err) {
  console.log(err);
}
