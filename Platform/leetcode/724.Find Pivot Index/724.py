from typing import List

class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
    for i in range(len(nums)):
      if (sum(nums[:i]) == sum(nums[i+1:])):
        return i
    return -1
  
# class Solution:
#    def pivotIndex(self, nums: List[int]) -> int:
#        """
#        method: iteration
#        complexity: O(n) / O(1)
#        """
#        left_sum, right_sum = -nums[-1], sum(nums)


#        for idx in range(len(nums)):
#            left_sum += nums[idx-1]
#            right_sum -= nums[idx]
#            if left_sum == right_sum:
#                return idx
#        return -1

s = Solution()
print(s.pivotIndex([1,7,3,6,5,6])) # 3
print(s.pivotIndex([1,2,3])) # -1
print(s.pivotIndex([2,1,-1])) # 0
print(s.pivotIndex([-1,-1,0,1,1,0])) # 5