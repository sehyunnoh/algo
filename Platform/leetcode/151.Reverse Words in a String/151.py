class Solution:
  def reverseWords(self, s: str) -> str:
    return " ".join([x for x in s.split(" ") if x != ''][::-1])
  
s = Solution()
print(s.reverseWords("the sky is blue"))
# print(s.reverseWords("  hello world  "))
# print(s.reverseWords("a good   example"))