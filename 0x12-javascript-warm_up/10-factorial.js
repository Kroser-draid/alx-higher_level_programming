#!/usr/bin/node
let num = Number(process.argv[2]);
let result = 1;
if (isNaN(num)) {
  console.log(result);
} else {
  function factorial (numb) {
    if (num <= 1) {
      return result;
    } else {
      result *= num;
      num = numb - 1;
      return factorial(num);
    }
  }
  console.log(factorial(num));
}
