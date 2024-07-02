#!/usr/bin/node
const size = Number(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let myString = '';
  for (let i = 0; i < size; i++) {
    myString += 'X';
  }
  for (let j = 0; j < size; j++) {
    console.log(myString);
  }
}
