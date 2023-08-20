function solution(image) {
  let row = image.length - 2;
  let col = image[0].length - 2;
  let result = Array(row).fill().map(() => Array(col).fill(0));
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      result[i][j]= ~~((image[i][j] + image[i][j+1] + image[i][j+2] +
                      image[i+1][j] + image[i+1][j+1] + image[i+1][j+2] +
                      image[i+2][j] + image[i+2][j+1] + image[i+2][j+2] ) / 9 )
    }
  }
    return result
}


solution = I => {
  //Slice off the border
  var B = I.slice(1,-1).map(e=>e.slice(1,-1))
  
  //Replace every element with the average
  // of its neighbors
  return B.map((row,i) =>
      row.map((elem,j) => {
          var sum = 0
          for(var x=0;x<3;++x)
              for(var y=0;y<3;++y)
                  sum += I[i+x][j+y]
          return sum/9|0
      })
  )
}


console.log(solution([[1,1,1], 
  [1,7,1], 
  [1,1,1]]));