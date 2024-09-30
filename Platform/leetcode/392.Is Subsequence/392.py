class Solution:
  # def isSubsequence(self, s: str, t: str) -> bool:
  #   if len(s) == 0: return True
  #   i = j = 0
  #   while (j < len(t)):
  #     if s[i] == t[j]:
  #       i += 1
  #       if len(s) == i:
  #         return True
  #     j += 1
  #   return False
  
  def isSubsequence(self, s: str, t: str) -> bool:
    if len(s) == 0: return True
    i = 0
    for char in t:
      if s[i] == char:
        i += 1
      if i == len(s):
        return True
    return False
  
  
s = Solution()
print(s.isSubsequence("abc", "ahbgdc")) # True
print(s.isSubsequence("axc", "ahbgdc")) # False
print(s.isSubsequence("", "ahbgdc")) # True
print(s.isSubsequence("abc", "ahbgdc")) # True