from typing import List
class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    result = []
    for num in range(rowIndex+1):
      if num <= 1:
        result.append([1] * (num + 1))
      else:
        prev = result[-1]
        result.append([1] + [prev[i] + prev[i+1] for i in range(len(prev)-1)] + [1])
    return result[rowIndex]
  # def getRow(self, rowIndex: int) -> List[int]:
  #   if rowIndex == 0:
  #     return [1]
  #   if rowIndex == 1:
  #     return [1, 1]
  #   prev = self.getRow(rowIndex - 1)
  #   return [1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1]
  
s = Solution()
print(s.getRow(3))