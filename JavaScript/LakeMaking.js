import { readFileSync } from 'fs';
const stdin = readFileSync("/dev/stdin").toString().trim().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();
console.log("here")
// const [r, c, e, n] = input().split(" ").map(Number)

// const arr = Array.from(Array(r), () => input().split(" ").map(Number))

// const sequence = Array.from(Array(n), () => input().split(" ").map(Number));

// console.log(r,c,e,n)
// console.log(arr)
// console.log(sequence)