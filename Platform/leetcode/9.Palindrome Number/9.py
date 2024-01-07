class Solution:
  def isPalindrome(self, x:int) -> bool:
    s = str(x)
    half = len(s)//2
    for i in range(half):
      if s[i] != s[-(1+i)]:
        return False
    return True
  
  
s = Solution()
# print(s.isPalindrome(121)) # true
# print(s.isPalindrome(-121)) # false
# print(s.isPalindrome(10)) # false
print(s.isPalindrome(1001)) # True