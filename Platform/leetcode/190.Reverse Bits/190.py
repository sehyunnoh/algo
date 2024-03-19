class Solution:
  def reverseBits(self, n: int) -> int:
    return int((bin(n)[2:].zfill(32))[::-1], 2)
  
s = Solution()
print(s.reverseBits(43261596))



