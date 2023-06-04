def solution(arr):
  return max([arr[i] * arr[i+1] for i in range(len(arr)-1)])


print(solution([3, 6, -2, -5, 7, 3]))