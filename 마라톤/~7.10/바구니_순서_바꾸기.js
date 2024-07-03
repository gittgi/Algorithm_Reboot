const fs = require('fs');
const stdin = fs.readFileSync("./input.txt").toString().trim().split("\n")
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [n, m] = input().split(" ").map(Number)

const arr = Array(m).fill(0).map(() => input().split(" ").map(Number))

answer = []
for (let i = 0; i <n+1; i++) {
  answer.push(i)
}

for (const [start, end, mid] of arr) {
  let back = answer.slice(mid, end+1)
  let front = answer.slice(start, mid)
  back.push(...front)
  answer.splice(start, end - start + 1, ...back)
}

console.log(answer.slice(1).join(" "))