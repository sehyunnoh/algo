import collections
from collections import Counter

class Solution:
  def closeStrings(self, word1: str, word2: str) -> bool:
    c1 = Counter(word1)
    c2 = Counter(word2)
    
    return c1 == c2 or (Counter(c1.values()) == Counter(c2.values()) and set(word1) == set(word2))
  
s = Solution()
# print(s.closeStrings('abc', 'bca'))
# print(s.closeStrings('cabbba', 'abbccc'))
print(s.closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff" ))