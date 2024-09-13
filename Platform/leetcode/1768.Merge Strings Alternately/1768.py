class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
    mn = min(len(word1), len(word2))
    result = []
    for i in range(mn):
      result.append(word1[i])
      result.append(word2[i])
    return ''.join(result)+(word1[mn:] if len(word1) > len(word2) else word2[mn:])
  
s = Solution()
print(s.mergeAlternately('ab','pqrs'))