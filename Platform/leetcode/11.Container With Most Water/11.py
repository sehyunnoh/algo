from typing import List

class Solution:
  # Time Limit Exceeded
  # def maxArea(self, height: List[int]) -> int:
  #   max_area = 0
  #   for i in range(len(height)):
  #     for j in range(i + 1, len(height)):
  #       max_area = max(max_area, min(height[i], height[j]) * (j - i))
  #   return max_area
  
  def maxArea(self, height: List[int]) -> int:
    i, j = 0, len(height) - 1
    max_area = 0
    while i < j:
      max_area = max(max_area, min(height[i], height[j]) * (j - i))
      if height[i] < height[j]:
        i += 1
      else:
        j -= 1
    return max_area 
  
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))