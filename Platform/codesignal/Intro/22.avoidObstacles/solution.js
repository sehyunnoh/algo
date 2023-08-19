function solution(arr) {
  arr.sort((a,b) => a-b)
  n = 2
  while( n < arr[arr.length-1]){
    let isDivided = false
    for (let x of arr){
      if (x%n === 0) {
        isDivided = true
        break 
      }
    }
    if (!isDivided) return n
    n++
  }
  return arr[arr.length-1]+1
}

function solution(arr) {
  for(var n=1;;n++) {if(arr.every(x=>x%n)) return n}
}

function solution(arr, k = 2) {
  return arr.every(e => e%k) ? k : solution(arr, k + 1);
}


function solution(inputArray) {
  var jump = 2;
  while (inputArray.some((obstacle) => obstacle % jump == 0)) {
    jump++;
  }
  return jump;
}

console.log(solution([5, 3, 6, 7, 9]));