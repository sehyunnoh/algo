def solution(s):
  result = 0
  for i in range(1, len(s)):
    if(s[i] <= s[i-1]):
      diff = s[i-1] - s[i] + 1
      result += diff
      s[i] += diff
  return result


print(solution([-1000, 0, -2, 0]))