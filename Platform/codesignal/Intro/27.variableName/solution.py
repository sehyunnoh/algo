import re

def solution2(name):
  if name[0].isdigit():
    return False
  return len([x for x in name if not (x.isdigit() or x == '_' or x.isalpha())]) == 0

def solution(name):
    return bool(re.match('[a-zA-Z_]\w*$', name))


print(solution("var_1__+Int")) # True