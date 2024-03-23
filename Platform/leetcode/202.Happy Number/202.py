class Solution:
  def isHappy(self, n:int) -> bool:
    s = set()
    while True:
      s.add(n)
      n = sum([int(x)**2 for x in str(n)])
      if n==1: return True
      if n in s: return False
      
  
s = Solution()
# print(s.isHappy(19)) # True
# print(s.isHappy(7)) # True
# print(s.isHappy(4)) # False
print(s.isHappy(2)) # False