class Solution:
  def removeStars(self, s: str) -> str:
    skip = 0
    result = []
    for i in range(len(s)-1,-1,-1):
      if s[i] == "*":
        skip += 1
      elif skip > 0:
        skip -= 1
      else:
        result.append(s[i])
    return ''.join(result[::-1])
    
  
  
s = Solution()
print(s.removeStars("leet**cod*e"))
# print(s.removeStarts("erase*****"))