#!/usr/bin/node
function add (a, b) {
  const pio = a + b;
  console.log(pio);
}

add(Number(process.argv[2]), Number(process.argv[3]));
