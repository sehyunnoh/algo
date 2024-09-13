from typing import List

class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    max_num = max(candies)
    return [ (x + extraCandies) >= max_num for x in candies]
  
  
s = Solution()
print(s.kidsWithCandies([2,3,5,1,3], 3))