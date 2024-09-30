class Solution:
  def maxVowels(self, s:str, k:int) -> int:
    vowels = ['a','e','i','o','u']
    num = len([x for x in s[:k] if x in vowels])
    max_num = num
    if num == k:
      return k
    for i in range(len(s)-k):
      if s[i] in vowels:
        num -= 1
      if s[i+k] in vowels:
        num += 1
      if num == k:
        return k
      max_num = max(max_num, num)
    return max_num
  
  
s = Solution()
# print(s.maxVowels("abciiidef", 3))
# print(s.maxVowels("aeiou", 2))
# print(s.maxVowels("leetcode", 3))
print(s.maxVowels("zpuerktejfp", 3))