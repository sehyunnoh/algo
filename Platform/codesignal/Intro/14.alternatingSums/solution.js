function solution(a) {
  let result = [0,0];
  a.forEach((v, i) => i %2 == 0 ? result[0] += v : result[1] += v);
  return result;
}

solution2 = a => a.reduce((p,v,i) => (p[i&1]+=v,p), [0,0])

console.log(solution([50, 60, 60, 45, 70]));