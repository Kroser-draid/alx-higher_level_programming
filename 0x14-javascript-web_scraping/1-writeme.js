#!/usr/bin/node

const path = process.argv[2];
const content = process.argv[3];
const fs = require('fs');

try {
  fs.writeFileSync(path, content, 'utf-8');
} catch (err) {
  console.log(err);
}
