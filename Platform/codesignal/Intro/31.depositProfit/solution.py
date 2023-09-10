def solution(d, r, t):
  year = 0
  while (d < t):
    d *= (1+r/100)
    year +=1
  return year


# print(solution(100, 20, 170))
print(solution(1, 1, 200))