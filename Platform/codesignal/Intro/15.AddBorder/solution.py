def solution(a):
  a= [f'*{x}*' for x in a ]
  star = '*' * len(a[0])
  a.insert(0, star)
  a.append(star)
  return a

print(solution(["abc", "ded"])) # ["*****", "*abc*", "*ded*", "*****"]