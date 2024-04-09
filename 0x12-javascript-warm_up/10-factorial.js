#!/usr/bin/node
function factorial (rav) {
  if (rav < 0) {
    return (-1);
  }
  if (rav === 0 || isNaN(rav)) {
    return (1);
  }
  return (rav * factorial(rav - 1));
}

console.log(factorial(Number(process.argv[2])));
