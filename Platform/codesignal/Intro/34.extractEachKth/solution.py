def solution(arr, k):
  return [ arr[i] for i in range(len(arr)) if (i + 1) % k != 0]

def solution(a, k):
  return [x for i, x in enumerate(a) if (i+1)%k !=0]

def solution(arr, k):
    del arr[k-1::k]
    return arr


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))