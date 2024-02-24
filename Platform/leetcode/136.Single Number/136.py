from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    nums.sort()
    for i in range(0, len(nums)-1, 2):
      if nums[i] != nums[i+1]:
        return nums[i]
    return nums[-1]
  
  
  
s = Solution()
print(s.singleNumber([2,2,1]))
print(s.singleNumber([4,1,2,1,2]))
print(s.singleNumber([1]))