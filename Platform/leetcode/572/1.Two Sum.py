from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    for i, num in enumerate(nums):
      if target - num in dic:
        return [dic[target - num], i]
      else:
        dic[num] = i


s = Solution()
print(s.twoSum([2,7,11,15], 9))