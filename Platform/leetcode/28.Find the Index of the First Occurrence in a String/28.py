class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    for i, x in enumerate(haystack):
      if needle[0] == x:
        if (i+len(needle)) > len(haystack):
          break
        if haystack[i:i+len(needle)] == needle:
          return i
    return -1
  
s = Solution()
print(s.strStr("sadbutsad", "sad"))

