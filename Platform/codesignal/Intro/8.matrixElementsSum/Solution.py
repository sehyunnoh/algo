def solution(m):
  result = 0
  for col in range(len(m[0])):
    for row in range(len(m)):
      val = m[row][col]
      if val == 0:
        break
      else:
        result += val
  return result
        
  
print(solution([[0,1,1,2], 
                [0,5,0,0], 
                [2,0,3,3]])) # 9