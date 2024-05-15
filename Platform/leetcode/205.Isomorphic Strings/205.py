class Solution:
  def isIsomorphic(self, s:str, t:str) -> bool:
    mapST, mapTS = {}, {}
    
    for c1, c2 in zip(s, t):
      if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
        return False
      mapST[c1] = c2
      mapTS[c2] = c1
    return True

  
s = Solution()
# print(s.isIsomorphic('egg','add'))
# print(s.isIsomorphic('foo','bar'))
# print(s.isIsomorphic('paper','title'))
print(s.isIsomorphic('badc','baba'))