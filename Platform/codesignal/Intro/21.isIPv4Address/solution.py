def checkNum(n):
  mok = 1
  while(n >= 10):
    n = n // 10
    mok += 1
  return mok

def solution(s):
  if s.count('.') != 3:
    return False
  for x in s.split('.'):
    if x == '':
      return False
    if not x.isdigit():
      return False
    if not (0 <= int(x) <= 255):
      return False
    if len(x) != checkNum(int(x)):
      return False
  return True


print(solution(".254.255.0"))