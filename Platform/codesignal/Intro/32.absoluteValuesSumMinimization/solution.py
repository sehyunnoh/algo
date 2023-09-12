import sys

def solution(a):
  min = sys.maxsize
  index = 0
  
  for i, x in enumerate(a):
    calculated = 0
    for y in a:
      calculated += abs(y-x)
    if calculated < min:
      min = calculated
      index = i
  return a[index]

def solution(A):
    return A[(len(A)-1)//2]


print(solution([2, 4, 7]))