# dynamic programming (fibonacci)
class Solution:
  def climbStairs(Self, n: int) -> int:
    first, second = 1, 1
    for _ in range(n-1):
      first, second = second, first+second
    return second
  
s = Solution()
print(s.climbStairs(2)) #2
print(s.climbStairs(3)) #3
