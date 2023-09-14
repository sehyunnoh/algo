def solution(m):
  w, h = len(m[0]), len(m)
  result = [[0 for _ in range(w)] for _ in range(h)]
  
  for r in range(h):
    for c in range(w):
      n = 0
      if (r-1 >= 0 and c-1 >= 0 and m[r-1][c-1]): n+=1
      if (r-1 >= 0 and m[r-1][c]): n+=1
      if (r-1 >= 0 and c+1 < w and m[r-1][c+1]): n+=1
      if (c+1 < w and m[r][c+1]): n+=1
      if (r+1 < h and c+1 < w and m[r+1][c+1]): n+=1
      if (r+1 < h and m[r+1][c]): n+=1
      if (r+1 < h and c-1 >=0 and m[r+1][c-1]): n+=1
      if (c-1 >= 0 and m[r][c-1]): n+=1
      result[r][c] = n
  return result

print(solution([[True,False,False], 
                [False,True,False], 
                [False,False,False]]))