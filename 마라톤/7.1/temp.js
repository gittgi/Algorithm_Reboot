const fs = require('fs');
console.log
const stdin = fs.readFileSync('./input.txt').toString().trim().split('\n')
const input = (() => {
  let line = 0;
  return () => stdin[line++]
})();

const k = parseInt(input())

const arr = input().split(" ").map(Number)
const answer = Array.from(Array(k), () => [])
console.log(parseInt(((2 ** k) - 1) / 2))

const recur = (s, e, depth) => {
  if (s === e) {
    answer[depth].push(arr[s])
    return
  }
  const m = parseInt((s + e) / 2)
  // console.log(s, e, m)
  answer[depth].push(arr[m])
  recur(s, m-1, depth+1)
  recur(m+1, e, depth+1)
}

recur(0, arr.length-1, 0)

console.log(answer.map(v => v.join(' ')).join('\n'));


// 완전이진트리가 아닌 포화이진트리