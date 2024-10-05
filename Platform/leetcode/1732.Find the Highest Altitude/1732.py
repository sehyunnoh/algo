from typing import List

class Solution:
  def largestAltitude(self, gain:List[int]) -> int:
    acc, max_num = 0, 0
    for x in gain:
      acc += x 
      max_num = max(max_num, acc)
    return max_num
  
s = Solution()
print(s.largestAltitude([-5,1,5,0,-7]))