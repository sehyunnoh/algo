from typing import List

class Solution:
  def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    return [
      [x for x in set(nums1) if x not in nums2],
      [x for x in set(nums2) if x not in nums1]
    ]
  
  
s = Solution()
# print(s.findDifference([1,2,3], [2,4,6]))
print(s.findDifference([1,2,3,3], [1,1,2,2]))