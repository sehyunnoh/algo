class Solution:
  def titleToNumberFromBack(self, columnTitle: str) -> int:
    result = 0
    for i in range(len(columnTitle)):
      result += ((26 ** i) * (ord(columnTitle[-(i+1)]) - 64))
      print(result)
    return result
  
  def titleToNumberFromFront(self, columnTitle: str) -> int:
    result = 0
    for i in range(len(columnTitle)):
        result += ((26 ** (len(columnTitle)-1-i)) * (ord(columnTitle[i]) - 64))
        print(result)
    return result
  
s = Solution()
# print(s.titleToNumber("ZY"))
# print(s.titleToNumberFromFront("AA"))
# print(s.titleToNumberFromBack("AA"))
# print(s.titleToNumberFromFront("ZY")) # 676 + 25 = 701
# print(s.titleToNumberFromBack("ZY")) # 25 + 676 = 701
print(s.titleToNumberFromFront("AZY")) # 676 + 676 + 25 = 701
print(s.titleToNumberFromBack("AZY")) # 25 + 676 + 676 = 1377