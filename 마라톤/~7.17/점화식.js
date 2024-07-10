const fs = require('fs');
const stdin = fs.readFileSync("./input.txt").toString().trim().split("\n")
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const n = parseInt(input())

const t = Array(35).fill(0).map(BigInt)
t[0] = BigInt(1)
t[1] = BigInt(1)

for (let i = 2; i < n+1; i++) {
  let num = BigInt(0)
  for (let j = 0; j < i; j++) {
    num += (t[j] * t[i-j-1])
  }

  t[i] = num
}

console.log(t[n].toString())

// 값이 크기 때문에 BigInt -> 뒤에 n 붙는 것 때문에 .toString()으로 출력...