# Time complexity: O(min(len(str1, len(str2))))
# Space complexity: O(len(str1) + len(str2))


class Solution:
  def gcdOfStrings(self, str1:str, str2:str) -> str:
    min_str = min(str1, str2)
    l1, l2 = len(str1), len(str2)
    for i in range(len(min_str), 0, -1):
      result = min_str[:i]
      lr = len(result)
      if ((l1 % lr) == 0 and 
          (l2 % lr) == 0 and
          (result * (l1 // lr)) == str1 and 
          (result * (l2 // lr)) == str2):
        return result
    return ''
  
s = Solution()
print(s.gcdOfStrings('ABCABC', 'ABC'))
print(s.gcdOfStrings('ABABAB', 'ABAB'))