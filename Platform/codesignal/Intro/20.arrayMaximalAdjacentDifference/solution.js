function solution(arr){
  let result = 0
  for(let i=1; i<arr.length; i++) {
    result = Math.max(result, Math.abs(arr[i] - arr[i-1]))
  }
  return result
}

function solution(arr) {
  return Math.max(...arr.slice(1).map((x,i)=>Math.abs(x-arr[i])))
}


console.log(solution([2, 4, 1, 0]));