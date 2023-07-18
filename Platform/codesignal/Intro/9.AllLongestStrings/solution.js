function solution(arr) {
  return arr.filter((x) => x.length === arr.map((x) => x.length).sort((a,b) => b-a)[0])
}

console.log(solution(["aba", "aa", "ad", "vcd", "aba"]));