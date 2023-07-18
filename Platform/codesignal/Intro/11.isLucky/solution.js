function solution(n) {
  let half = (""+n).length / 2
  return (""+n).slice(0, half).split("").map(x => +x).reduce((a,b) => (a+b), 0) === (""+n).slice(half).split("").map(x => +x).reduce((a,b) => (a+b), 0)
}

function solution2(n) {
  let arr = ("" + n).split("");
  let result = 0;
  for (let i = 0; i < arr.length / 2; i++) {
    result += +arr[i] - arr[arr.length - 1 - i];
  }
  return result === 0 ? true : false;
}

console.log(solution(1230));