const fs = require('fs');
const stdin = fs.readFileSync("./input.txt").toString().trim().split("\n")
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();


const t = parseInt(input())

for (let i=1; i<t+1; i++) {
  const n = parseInt(input())
  const arr = input().split(" ").map(Number)
  const categoryMap = new Map();
  let idx = 0
  for (let j=0; j<arr.length; j++) {
    let no = arr[j]
    if (categoryMap.has(no)) {
      categoryMap.set(no, categoryMap.get(no) + 1)
    } else {
      categoryMap.set(no, 1)
      idx = j
    }
  }

  console.log(`Case ${i}: ${idx + 1}`)
}