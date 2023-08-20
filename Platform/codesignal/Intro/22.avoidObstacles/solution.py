def solution(arr):
  arr.sort()
  for x in range(2, arr[-1]):
    is_divided = False
    for n in arr:
      if n % x == 0:
        is_divided = True
        break
    if not is_divided:
      return x
  return arr[-1]+1

def solution3(arr):
  n = 2
  while(True):
    if all([x%n>0 for x in arr]):
      return n
    n+=1

def solution(inputArray):
    return min([i for i in range(2, max(inputArray)+2) if all([j%i!=0 for j in inputArray])])

print(solution3([10, 12]))
# print(solution3([5, 3, 6, 7, 9]))
# print(solution([3, 4, 5, 6, 7, 8, 9, 10]))