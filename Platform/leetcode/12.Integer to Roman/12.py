class Solution:
  def intToRoman(self, num: int) -> str:
    map = {
      1000: 'M',
      500: 'D',
      100: 'C',
      50: 'L',
      10: 'X',
      5: 'V',
      1: 'I'
    }
    res = ''
    for key in map:
      while num >= key:
        c = str(num)[0]
        if c in ['4', '9']:
          d = 10 ** (len(str(num)) - 1)
          res += map[d]
          temp = d + (int(c) * d)
          res += map[temp]
          num -= (int(c) * d)
        else:
          res += map[key]
          num -= key
    return res

s = Solution()
# print(s.intToRoman(3)) # "III"
print(s.intToRoman(3749)) # "MMMDCCXLIX"