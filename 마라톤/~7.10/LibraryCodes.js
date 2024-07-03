const fs = require('fs');
const stdin = fs.readFileSync("./input.txt").toString().trim().split("\n")
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();


while (true) {
  const [library, f] = input().split(" ")
  if (library === '#') {
    break
  }
  console.log(library, "Library")
  const n = parseInt(input())

  for (i=0; i<n; i++) {
    let [w, char] = input().split(" ")
    w = parseInt(w)
    if (w >= char.length * f + 2) {
      console.log("Book", i+1, "horizontal")
    } else {
      console.log("Book", i+1, "vertical")
    }


    
  }

}