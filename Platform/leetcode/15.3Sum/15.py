from typing import List

class Solution:
  # time limit exceeded
  # def threeSum(self, nums: List[int]) -> List[List[int]]:
  #   res = []
  #   for i in range(len(nums)):
  #     for j in range(i+1, len(nums)):
  #       for k in range(j+1, len(nums)):
  #         if (nums[i] + nums[j] + nums[k]) == 0:
  #           sorted_arr = sorted([nums[i], nums[j], nums[k]])
  #           if sorted_arr not in res:
  #             res.append(sorted_arr)
  #   return res
  pass
          
  
  
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))