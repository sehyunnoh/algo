def solution(s):
  start, end = 0, 0
  while True:
    if '(' not in s:
      return s
    for i, x in enumerate(s):
      if x == '(':
        start = i
      elif x == ')':
        end = i
        s = s[:start] + s[start+1:end][::-1] + s[end+1:]
        break
      
      
      
def solution2(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return solution2(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s

print(solution("a(bc(de))"))