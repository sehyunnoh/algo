class Solution:
  def lengthOfLastWorld(self, s: str) -> int:
    return len(s.strip().split(' ')[-1])
  

s = Solution()
# print(s.lengthOfLastWorld("Hello World")) 
print(s.lengthOfLastWorld("   fly me   to   the moon  ")) #4