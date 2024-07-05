const fs = require('fs');
const stdin = fs.readFileSync("./input.txt").toString().trim().split("\n")
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const n = parseInt(input())

const arr = input().split(" ").map(Number)

arr.sort((a, b) => a - b)

console.log(arr[2*n-1] - arr[n])