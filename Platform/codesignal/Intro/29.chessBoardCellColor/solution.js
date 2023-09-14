function solution(c1, c2) {
  return Math.abs((c2.charCodeAt(0) - c1.charCodeAt(0))%2) === Math.abs((c2[1] - c1[1])%2);
}



console.log(solution('A1', 'C3'));