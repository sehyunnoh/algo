function solution(d, r, t) {
  let year = 0;
  while (d < t) {
    d *= ( 1 + r/100)
    year++;
  }
  return year;
}

console.log(solution(100, 20, 170));