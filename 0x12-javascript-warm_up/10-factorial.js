#!/usr/bin/node
const num = Number(process.argv[2]);
let result = 1;
if (isNaN(num)) {
  console.log(result);
} else {
  function factorial (numb) {
    if (numb <= 1) {
      return result;
    } else {
      result *= numb;
      return factorial(numb - 1);
    }
  }
  console.log(factorial(num));
}
