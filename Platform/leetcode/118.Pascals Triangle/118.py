from typing import List

# class Solution:
#   def generate(self, numRows: int) -> List[List[int]]:
#     result = []
#     for i in range(1, numRows + 1):
#       result.append([1] * i)
#       for j in range(1, i - 1):
#         result[i - 1][j] = result[i - 2][j - 1] + result[i - 2][j]
        
#     return result
    
    
class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    result = []
    for i in range(1, numRows + 1):
      if i <= 2:
        result.append([1] * i)
      else:
        prev = result[-1]
        result.append([1] + [prev[i]+prev[i+1] for i in range(len(prev) - 1)] + [1])
        
    return result
  
  
s = Solution()
print(s.generate(5))