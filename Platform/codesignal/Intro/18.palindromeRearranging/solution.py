def solution(s):
  return len([x for x in [s.count(x) for x in set(s)] if x % 2 != 0]) <= 1

def solution(s):
  return sum([s.count(x)%2 for x in set(s)]) <= 1

# print(solution("abbcabb")) # True
# print(solution("aaabbb")) # True
print(solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbcccc")) # True