from typing import List

class Solution:
  # Time Limit Exceeded
  # def maxProfit(self, prices: List[int]) -> int:
  #   gap = 0
  #   for i in range(len(prices)-1):
  #     for j in range(i+1, len(prices)):
  #       if prices[j] - prices[i] > gap:
  #         gap = prices[j] - prices[i]
  #   return gap
  
  # Time Limit Exceeded
  # def maxProfit(self, prices: List[int]) -> int:
  #   result = 0
  #   for i, x in enumerate(prices[:-1]):
  #     gap = max(prices[i+1:]) - x
  #     if gap > result:
  #       result = gap
  #   return result
  
  def maxProfit(self, prices: List[int]) -> int:
    l, r, max_gap = 0, 1, 0
    while r < len(prices):
        gap = prices[r] - prices[l]
        if gap < 0:
            l = r
        else:
            max_gap = max(max_gap, gap)
        r += 1
    return max_gap
      
  

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))