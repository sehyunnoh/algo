from typing import List

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    i = j = 0
    while (j < len(nums)):
      if nums[i] == 0:
        if nums[j] != 0:
          nums[i], nums[j] = nums[j], nums[i]
          i += 1
      else:
        i += 1
      j += 1
      
# class Solution:
#   def moveZeroes(self, nums: List[int]) -> None:
#     i = 0
    
#     for j in range(len(nums)):
#       if nums[j] != 0:
#         nums[i] = nums[j]
#         i += 1
      
#     for j in range(i, len(nums)):
#       nums[j] = 0

s = Solution()
print(s.moveZeroes([0,1,0,3,12]))