import re

def solution(s):
  for x in s:
    if x.isdigit():
      return x
    
def solution2(s):
  return re.search('\d', s).group()

def solution3(s):
  for x in s:
    if '0' <= x <= '9':
      return x


print(solution("var_1__Int")) #1