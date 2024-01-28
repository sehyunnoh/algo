class Solution:
  def mySqrt(self, x: int) -> int:
    if x == 0: return 0
    n = 2
    while n*n <= x:
      n += 1
    return n - 1
    
  
  
s = Solution()
print(s.mySqrt(4)) #2
print(s.mySqrt(8)) #2
