function solution(a) {
  let people = a.filter( x=> x !== -1).sort((a,b) => a-b);
  a.forEach((x,i) => {
    if(x !== -1) {
      a[i] = people.shift();
    }
  })
  return a;
}

function solution2(a) {
  let arr = a.filter((x) => x != -1).sort((a, b) => a - b);
  let cnt = 0;
  return a.map((x) => (x === -1 ? -1 : arr[cnt++]));
}

console.log(solution([-1, 150, 190, 170, -1, -1, 160, 180]));