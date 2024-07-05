const fs = require('fs');
const stdin = fs.readFileSync("./input.txt").toString().trim().split("\n")
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();


const t = parseInt(input())

for (let i=1; i<t+1; i++) {
  const [r, t] = input().split(" ").map(Number)


  let paint = (2 * r) + 1

  let last = paint
  let cnt = 1
  while (true) {
    const newPaint = last + 4
    if (paint + newPaint <= t) {
      cnt += 1
      paint += newPaint
      last = newPaint
    } else {
      break
    }
    
  }

  console.log(`Case #${i}: ${cnt}`)





}

