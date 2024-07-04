#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const number = [];
  const length = process.argv.length;
  for (let i = 2; i < length; i++) {
    number.push(Number(process.argv[i]));
  }
  number.sort((a, b) => a - b);
  console.log(number[number.length - 2]);
}
