def solution(n):
  half = len(str(n))//2
  return sum([int(x) for x in str(n)[:half]]) == sum([int(x) for x in str(n)[half:]])


print(solution(1230))