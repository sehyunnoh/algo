def solution(n):
  half = len(str(n))//2
  return sum([int(x) for x in str(n)[:half]]) == sum([int(x) for x in str(n)[half:]])


def solution2(n):
  result = 0
  s = str(n)
  for i in range(len(s) // 2):
    result += (int(s[i]) - int(s[-1-i]))
  return result == 0

print(solution(1230))