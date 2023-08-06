function solution(series) {
  var moves = 0;
  
  for (var i = 1; i < series.length; i++) {
      if (series[i] <= series[i - 1]) {
          diff = series[i - 1] - series[i] + 1;
          series[i] += diff;
          moves += diff;
      }
  }
  
  return moves;
}

// console.log(solution([1,1,1]));
console.log(solution([-1000, 0, -2, 0]));