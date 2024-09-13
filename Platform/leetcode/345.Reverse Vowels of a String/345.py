class Solution:
  def reverseVowels(Self, s: str) -> str:
    vowels, arr = ['a','e','i','o','u'], []
    for x in s:
      if x.lower() in vowels:
        arr.append(x)
    return ''.join([arr.pop() if x.lower() in vowels else x for x in s])
    
  
  
s = Solution()
print(s.reverseVowels("IceCreAm"))