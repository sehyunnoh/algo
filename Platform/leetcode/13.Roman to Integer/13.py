class Solution:
  ROMAN = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
  }
  def romanToInt(self, s:str) -> int:
    result = 0
    prev = ''
    for v in s:
      result += self.ROMAN[v]
      if prev == 'I' and (v in ['V','X']):
        result -= (self.ROMAN['I'])*2
      elif prev == 'X' and (v in ['L','C']):
        result -= (self.ROMAN['X']*2)
      elif prev == 'C' and (v in ['D','M']):
        result -= (self.ROMAN['C']*2)
      prev = v
    return result
  
  

s = Solution()
# print(s.romanToInt("III")) #3
print(s.romanToInt("MCMXCIV")) #1994