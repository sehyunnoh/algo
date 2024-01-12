from typing import List

# class Solution:
#   def removeDuplicates(self, nums: List[int]) -> int:
#     return len(set(nums))
  
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#           s = set(nums)
#           nums.clear()
#           for i in s:
#                nums.append(i)
#           nums.sort()
#           return len(nums)

class Solution:
  def removeDuplicates(self, nums):
      i,j=0,1
      while i<=j and j<len(nums):
          if nums[i]==nums[j]:
              del nums[j]
          else:
              i+=1
              j+=1
      return len(nums)
  
s = Solution()
print(s.removeDuplicates([1,1,2]))
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))