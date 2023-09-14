function solution(n){
  return n.toString().split('').every((x) => x%2 === 0)
}

console.log(solution(248622));