def solution(arr):
  return [x for x in arr if len(x) == max([len(x) for x in arr])]


print(solution(["aba", 
 "aa", 
 "ad", 
 "vcd", 
 "aba"])) 