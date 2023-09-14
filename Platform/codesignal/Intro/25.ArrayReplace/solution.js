function solution(a, e, s) {
  return a.map((x) => x === e ? s : x);
}

console.log(solution([1, 2, 1], 1, 3));