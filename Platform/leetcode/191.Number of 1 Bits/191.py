class Solution:
  # def hammingWeight(self, n: int) -> int:
  #   return (bin(n)[2:]).count('1')
  
  # def hammingWeight(self, n: int) -> int:
  #   return len((bin(n)[2:]).replace('0',''))
  
  # def hammingWeight(self, n: int) -> int:
  #   result = 0
  #   while n>0:
  #     result += n%2
  #     n //=2
  #   return result
  
  # def hammingWeight(self, n: int) -> int:
  #   res = 0
  #   while n:
  #     res += n % 2
  #     n = n >> 1
  #   return res
  
  def hammingWeight(self, n: int) -> int:
    res = 0
    while n:
      n = n & (n-1)
      res += 1
    return res
  

  
s = Solution()
print(s.hammingWeight(11))
print(s.hammingWeight(128))
print(s.hammingWeight(2147483645))
