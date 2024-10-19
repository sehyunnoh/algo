from typing import List

# class Solution:
#   def equalPairs(Self, grid: List[List[int]]) -> int:
#     columns = [ list(x) for x in zip(*grid)]
#     result = 0
    
#     for col_arr in columns:
#       for row_arr in grid:
#         if col_arr == row_arr:
#           result += 1
#     return result 
    

class Solution:
   def equalPairs(self, grid: List[List[int]]) -> int:
       n = len(grid)
       from collections import defaultdict
       if n == 1:
           return 1
      
       row_hash = defaultdict(int)
       col_hash = defaultdict(int)


       for i in range(n):
           row_string = ','.join([str(x) for x in grid[i]])  # ‘3,1,2,2’
           col_string = ','.join([str(grid[k][i]) for k in range(n)])
           row_hash[row_string] += 1
           col_hash[col_string] += 1
      
       res = 0
       for key, value in row_hash.items():
           if key in col_hash:
               res += value * col_hash[key]
       return res
     
  
  
s = Solution()
# print(s.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))