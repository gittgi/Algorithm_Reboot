const fs = require('fs');
const stdin = fs.readFileSync("./input.txt").toString().trim().split("\n")
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();


const [h, w] = input().split(" ").map(Number)

const b1 = Array.from(Array(h), () => input().split(" ").map(Number))
const b2 = Array.from(Array(h), () => input().split(" ").map(Number))

const dp = Array.from(Array(h), () => Array(w).fill(0))

for (let i = 0; i < w; i++) {
  dp[0][i] = (b1[0][i] - b2[0][i]) ** 2
  
}

for (let i = 1; i < h; i++) {
  for (let j = 0; j < w; j++) {
    let minVal = Infinity
    for (let k = Math.max(0, j-1); k < Math.min(j+2, w); k++) {
      minVal = Math.min(dp[i-1][k], minVal)
    }
    dp[i][j] = minVal + ((b1[i][j] - b2[i][j]) ** 2)
  }
}

console.log(Math.min(...dp[h-1]))
