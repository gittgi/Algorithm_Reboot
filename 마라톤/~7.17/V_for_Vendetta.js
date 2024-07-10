const fs = require('fs');
const stdin = fs.readFileSync("./input.txt").toString().trim().split("\n")
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const arr = input().split(" ").map(Number)

for (const t of arr) {
  const answer = Array.from(Array(t), () => Array(2*t - 1).fill(" "))
  answer[t-1][t-1] = "*"
  let left = t - 1
  let right = t - 1
  for (let i = t-2; i >= 0; i--) {
    left -= 1
    right += 1
    answer[i][left] = "*"
    answer[i][right] = "*"
  }
  for (let i = 0; i < t; i++) {
    console.log(answer[i].join("").trimEnd()) //백준에서는 뒷쪽 공백은 출력형식 에러 뜸
  }
}
