from typing import List

class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
    for i in range(len(nums)):
      if (sum(nums[:i]) == sum(nums[i+1:])):
        return i
    return -1

s = Solution()
print(s.pivotIndex([1,7,3,6,5,6])) # 3
print(s.pivotIndex([1,2,3])) # -1
print(s.pivotIndex([2,1,-1])) # 0
print(s.pivotIndex([-1,-1,0,1,1,0])) # 5