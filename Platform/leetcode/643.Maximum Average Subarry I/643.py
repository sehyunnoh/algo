from typing import List

class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    max_val = sum_val = sum(nums[:k])
    for i in range(len(nums)-k):
      sum_val = sum_val-nums[i]+nums[i+k]
      max_val = max(max_val, sum_val)
    return max_val / k
      
  
  
s = Solution()
# print(s.findMaxAverage([1,12,-5,-6,50,3], 4))
print(s.findMaxAverage([5], 1))