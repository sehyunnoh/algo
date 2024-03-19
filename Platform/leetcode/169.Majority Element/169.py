from typing import List

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    arr = [{x: nums.count(x)} for x in set(nums)]
    return [k for item in arr for k, v in item.items() if v > len(nums)//2][0]
  
    
s = Solution()
# print(s.majorityElement([3,2,3]))
# print(s.majorityElement([2,2,1,1,1,2,2]))
print(s.majorityElement([-1,1,1,1,2,1]))