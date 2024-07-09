const fs = require('fs');
const stdin = fs.readFileSync("./input.txt").toString().trim().split("\n")
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();


const n = parseInt(input())
const arr1 = []
const arr2 = []




if (n % 3 === 0) {
    const num = Math.floor(n / 3)
    for (let i = 0; i < num; i++) {
      arr1.push((i*3) + 1)
      arr1.push((i*3) + 2)
      arr2.push((i*3) + 3)
  }
} else if (n % 3 == 2) {
  arr1.push(1)
  arr2.push(2)
  const num = Math.floor(n / 3)
  for (let i = 0; i < num; i++) {
    arr1.push(((i+1)*3))
    arr1.push(((i+1)*3)+1)
    arr2.push(((i+1)*3)+2)
  }

} else {
  const num = Math.floor(n / 3)
  for (let i = 0; i < num; i++) {
    arr1.push((i*3) + 2)
    arr1.push((i*3) + 3)
    arr2.push((i*3) + 4)

  }

}

    


console.log(arr1.length)
console.log(arr1.join(" "))
console.log(arr2.length)
console.log(arr2.join(" "))