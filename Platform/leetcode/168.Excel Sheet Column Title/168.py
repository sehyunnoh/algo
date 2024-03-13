class Solution:
  def convertToTitle(self, num: int) -> str:
    result = []
    while num > 26:
      if num%26 == 0:
        result.append(26)
        num = num//26 - 1
      else:
        result.append(num%26)
        num //= 26
    result = result[::-1]
    return ''.join([chr(x+64) for x in ([num]+result)])
  
s = Solution()
print(s.convertToTitle(1)) # 'A'
print(s.convertToTitle(28)) # 'AB'
print(s.convertToTitle(701)) # 'ZY'
print(s.convertToTitle(2147483647)) # 
print(s.convertToTitle(52)) # 
