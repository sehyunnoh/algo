def solution(year):

  val = year // 100
  return val+1 if (year % 100 > 0) else val


print(solution(1905))