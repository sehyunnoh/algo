from typing import List

class Solution:
  def equalPairs(Self, grid: List[List[int]]) -> int:
    columns = [ list(x) for x in zip(*grid)]
    result = set()
    
    for c, col_arr in enumerate(columns):
      for r, row_arr in enumerate(grid):
        if col_arr == row_arr:
          result.add((r, c))
    return len(result)
    
    
  
  
s = Solution()
# print(s.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))