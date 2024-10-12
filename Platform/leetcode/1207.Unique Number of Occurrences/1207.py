from typing import List

class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    s = set(arr)
    return len(s) == len(set([arr.count(x) for x in s]))
  
  
s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))