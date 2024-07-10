const fs = require('fs');
const stdin = fs.readFileSync("./input.txt").toString().trim().split("\n")
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();


const t = parseInt(input())
for (let testcase = 1; testcase < t+1; testcase++) {
  let [n, d, c, m] = input().split(" ").map(Number)
  const arr = input()
  let dogCnt = 0
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "D") {
      dogCnt += 1
    }
  }
  
  for (let i = 0; i < arr.length; i++) {
    let now = arr[i]
    if (now === "C") {
      if (c === 0) {
        break
      }
      c -= 1
    } else {
      if (d === 0) {
        break
      }
      d -= 1
      c += m
      dogCnt -= 1
    }
    
  }
  if (dogCnt === 0) {
    console.log("Case #" + testcase + ": YES")
  } else {
    console.log("Case #" + testcase + ": NO")
  }


}