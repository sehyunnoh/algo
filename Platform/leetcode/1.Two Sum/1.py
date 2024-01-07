from typing import List

# class Solution:
#   def twoSum(self, nums: List[int], target: int) -> List[int]:
#     dic = {}
#     for i, num in enumerate(nums):
#       if target - num in dic:
#         return [dic[target - num], i]
#       else:
#         dic[num] = i


# class Solution:
#   def twoSum(self, nums: List[int], target: int) -> List[int]:
#     for i in range(len(nums)):
#       for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#           return [i, j]
        
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    for i, v in enumerate(nums):
      if (target - v) in dic.keys():
        return [dic[target-v], i]
      else:
        dic[v] = i

s = Solution()
print(s.twoSum([2,7,11,15], 9))