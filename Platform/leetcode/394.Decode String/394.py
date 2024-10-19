class Solution:
  def decodeString(self, s: str) -> str:
    stack = []
    for x in s:
      if x == ']':
        ch = ''
        while stack[-1] != '[':
          ch = stack.pop() + ch
        stack.pop()
        num = ''
        while stack and stack[-1].isdigit():
          num = stack.pop() + num
        stack.append(int(num) * ch)
      else:
        stack.append(x)
    return ''.join(stack)
  
  
s = Solution()
# print(s.decodeString("3[a]2[bc]"))
# print(s.decodeString("3[a2[c]]"))
print(s.decodeString("2[abc]3[cd]ef"))