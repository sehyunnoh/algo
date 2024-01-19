from typing import List

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    start, end = 0, len(nums)-1
    while True:
      m = (start + end)//2
      if nums[m] == target:
        return m
      elif nums[m] > target:
        if end == m: break
        end = m
      else:
        if start == m: break
        start = m
    if target < nums[start]:
      return start
    elif target > nums[end]:
      return end + 1
    else:
      return end
      
        
  
  
s = Solution()
print(s.searchInsert([1,3,5,6], 5)) # 2
print(s.searchInsert([1,3,5,6], 2)) # 1
print(s.searchInsert([1,3,5,6], 7)) # 4
print(s.searchInsert([1,3,5,6], 0)) # 0
print(s.searchInsert([1], 0)) # 0
