from typing import List

class Solution:
  def maxOperations(self, nums: List[int], k: int) -> int:
    nums.sort()
    i, j = 0, len(nums)-1
    result = 0
    while i < j:
      plus = nums[i] + nums[j]
      if plus == k:
        result += 1
        i += 1
        j -= 1
      elif plus < k:
        i += 1
      else:
        j -= 1
    return result
        

s = Solution()
print(s.maxOperations([1,2,3,4], 5)) # 2
print(s.maxOperations([3,1,3,4,3], 6)) # 1