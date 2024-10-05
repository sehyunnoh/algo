from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        s, zero_num, max_num = 0, 0, 0
        for e in range(len(nums)):
            if nums[e] == 0:
                zero_num += 1
            while zero_num > 1:
                if nums[s] == 0:
                    zero_num -= 1
                s += 1
            max_num = max(max_num, e-s)
        return max_num
        
  
s = Solution()
print(s.longestSubarray([1,1,0,1])) # 3
print(s.longestSubarray([0,1,1,1,0,1,1,0,1])) # 5
print(s.longestSubarray([1,1,1])) # 2
