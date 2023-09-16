function solution(arr, k) {
  return arr.filter((_, i) => (i+1) % k != 0)
}

function solution(arr, k) {
  return arr.filter((_, i) => (i+1) % k)
}

console.log(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3));