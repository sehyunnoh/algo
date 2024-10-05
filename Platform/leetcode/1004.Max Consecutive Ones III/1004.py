from typing import List

class Solution:
  def longestOnes(self, nums: List[int], k: int) -> int:
    s, zero_num, max_num = 0, 0, 0
    for e in range(len(nums)):
        if nums[e] == 0:
            zero_num += 1
        while zero_num > k:
            if nums[s] == 0:
                zero_num -= 1
            s += 1
        max_num = max(max_num, e-s+1)
    return max_num
        
      
      
  
  
s = Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)) # 10