def solution(a, b):
  result = []
  diff = 0
  
  for i in range(len(a)):
    if a[i] != b[i]:
      diff += 1
      if diff > 2:
        return False
      result.extend([a[i], b[i]])
  return diff == 0 or (diff == 2 and result[0] == result[3] and result[1] == result[2])

def solution(a,b):
  return sorted(a) == sorted(b) and sum([1 for i in range(len(a)) if a[i] != b[i]]) < 3

def solution(a,b):
  return sorted(a) == sorted(b) and sum([a != b for a, b in zip(a,b)]) <= 2

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
# print(solution([1, 2, 1, 2], [2, 2, 1, 1]))