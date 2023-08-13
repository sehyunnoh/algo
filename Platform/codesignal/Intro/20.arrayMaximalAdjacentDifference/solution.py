def solution(arr):
  return max([abs(arr[i] - arr[i-1]) for i in range(1, len(arr))])

print(solution([-1, 4, 10, 3, -2]))