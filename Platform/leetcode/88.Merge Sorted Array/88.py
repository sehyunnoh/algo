from typing import List

class Solution:
  def merge(self, nums1: List[int], m:int, nums2: List[int], n:int) -> None:
    combined = sorted(nums1[:m] + nums2[:n])
    nums1.clear()
    for x in combined:
      nums1.append(x)
  
s = Solution()
print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
  