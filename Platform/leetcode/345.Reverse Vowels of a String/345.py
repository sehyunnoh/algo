class Solution:
  def reverseVowels(Self, s: str) -> str:
    vowels, arr = ['a','e','i','o','u','A','E','I','O','U'], []
    for x in s:
      if x in vowels:
        arr.append(x)
    return ''.join([arr.pop() if x in vowels else x for x in s])
    
  
  
s = Solution()
print(s.reverseVowels("IceCreAm"))