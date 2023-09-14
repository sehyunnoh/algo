function solution(m){
  const [row, col] = [m.length, m[0].length]
  let result = Array(row).fill().map(() => Array(col).fill(0))

  for (let r=0; r<row; r++) {
    for (let c=0; c<col; c++) {
      let num = 0;
      if (r-1 >=0 && c-1 >=0 && m[r-1][c-1]) num++
      if (r-1 >=0 && m[r-1][c]) num++
      if (r-1 >=0 && c+1 < col && m[r-1][c+1]) num++
      if (c+1 < col && m[r][c+1]) num++
      if (r+1 < row && c+1 < col && m[r+1][c+1]) num++
      if (r+1 < row && m[r+1][c]) num++
      if (r+1 < row && c-1 >=0 && m[r+1][c-1]) num++
      if (c-1 >=0 && m[r][c-1]) num++
      result[r][c] = num
    }
  }
  return result
}

console.log(solution([[true,false,false], 
                      [false,true,false], 
                      [false,false,false]]));