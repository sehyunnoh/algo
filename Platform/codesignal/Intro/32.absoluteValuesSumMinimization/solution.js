function solution(a) {
  let [min, index] =  [Number.MAX_VALUE, 0];
  for (let i=0; i<a.length; i++) {
    let sum = 0;
    for (let j=0; j<a.length; j++) {
      if (i === j) continue;
      sum += Math.abs(a[j] - a[i])
    }
    if (sum < min) {
      min = sum;
      index = i;
    }
  }
  return a[index];
}

function solution(A) {
  return A[Math.ceil(A.length/2)-1];
}


console.log(solution([2, 4, 7]));