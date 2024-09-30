from typing import List

class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    i, j = 0, k-1
    max_val = sum_val = sum(nums[:k])
    for _ in range(len(nums)-k):
      sum_val = sum_val-nums[i]+nums[j+1]
      max_val = max(max_val, sum_val)
      i += 1
      j += 1
    return max_val / k
      
  
  
s = Solution()
# print(s.findMaxAverage([1,12,-5,-6,50,3], 4))
print(s.findMaxAverage([5], 1))