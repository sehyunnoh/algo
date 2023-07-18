function solution(m) {
  let sum = 0;
  for (let c=0; c < m[0].length; c++) {
    for (let r=0; r < m.length; r++){
      if (m[r][c] === 0){
        break;
      } else {
        sum += m[r][c];
      }
    }
  }
  return sum;
}

console.log(solution([[0, 1, 1, 2], 
                      [0, 5, 0, 0], 
                      [2, 0, 3, 3]]));