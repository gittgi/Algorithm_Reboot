const fs = require('fs');
const stdin = fs.readFileSync("./input.txt").toString().trim().split("\n")
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const n = parseInt(input())
const answer = Array.from(Array(n), () => Array(n).fill("."))
const horizontal = Array.from(Array(n), () => Array(n).fill(false))
const vertical = Array.from(Array(n), () => Array(n).fill(false))
const order = input()

const direction = {"D": [1, 0], "R":[0, 1], "U":[-1, 0], "L":[0, -1]}
let [x, y] = [0, 0]
if (!order) {
  for (const i of answer) {
    console.log(i.join(""))
  }
} else {
  for (const d of order) {
    const [dx, dy] = direction[d]
    if (x + dx < 0 || x +dx >= n || y + dy < 0 || y + dy >= n) {
      continue
    }
  
    if (d === "U" || d === "D") {
      vertical[x][y] = true
      vertical[x+dx][y+dy] = true
    } else {
      horizontal[x][y] = true
      horizontal[x+dx][y+dy] = true
    }
    x += dx
    y += dy
  }
  
  
  for (let i=0; i<n; i++) {
    for (let j=0; j<n; j++) {
      if (horizontal[i][j] && vertical[i][j]) {
        answer[i][j] = "+"
      } else if (horizontal[i][j] && !vertical[i][j]) {
        answer[i][j] = "-"
      } else if (!horizontal[i][j] && vertical[i][j]) {
        answer[i][j] = "|"
      }
    }
  }
    
  
  for (const i of answer) {
    console.log(i.join(""))
  }
}
