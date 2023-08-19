function solution(s) {
  arr = s.split('.')
  if (arr.length !== 4) return false
  return arr.map(x => {
    if (isNaN(x)) return false;
    if (x === "") return false;
    if (x < 0 || x > 255) return false;
    if (x.length !== LenNum(x)) return false;
    return true
  }).every(x=>x)
}

function LenNum(x) {
  let result = 1;
  while(x >= 10) {
    x = ~~(x/10)
    result++
  }
  return result
}
// console.log(solution("172.16.254.14"));
// console.log(solution(".254.255.0"));
console.log(solution("00.1.1.1a"));