# class Solution:
#   def isValid(self, s:str) -> bool:
#     res = []
#     p = {'(':')', '[':']', '{':'}'}
#     for x in s:
#       if x in p.keys():
#         res.append(x)
#       else:
#         if len(res) == 0:
#           return False
#         if p[res.pop()] != x:
#           return False
#     return len(res) == 0
    
class Solution:
  def isValid(self, s:str) -> bool:
    close_to_open = {
      ")": "(",
      "}": "{",
      "]": "[",
    }
    
    stack = []
    for brace in s:
      if brace not in close_to_open:
        stack.append(brace)
      else:
        stack_top_element = stack.pop() if stack else 'F'
        
        if close_to_open[brace] != stack_top_element:
          return False
    return not stack

    
s = Solution()
# print(s.isValid("()[]{}"))
print(s.isValid("]"))