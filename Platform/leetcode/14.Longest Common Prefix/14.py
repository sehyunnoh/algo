from typing import List

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         strs.sort(key = lambda x: len(x))

#         length = len(strs[0])
#         max = ''
#         for i in range(length):
#             com = ''
#             for j in range(length):
#                 v = strs[0][j]
#                 com += v
#                 if all([com in x for x in strs]):
#                     if len(com) > len(max):
#                         max = com
#                 else:
#                     break
#         return max

# class Solution:
#   def longestCommonPrefix(self, strs: list[str]) -> str:
#     strs.sort(key=lambda x: len(x))
#     length = len(strs[0])
#     result = ''
#     for i in range(length):
#       s = set()
#       for x in strs:
#         s.add(x[i])
#       if len(s) > 1:
#         return result
#       else:
#         result += x[i]
#     return result
  
  
# class Solution:
#     def longestCommonPrefix(self, v: List[str]) -> str:
#         ans=""
#         v=sorted(v) # sorted alphabetically
#         first=v[0]
#         last=v[-1]
#         for i in range(min(len(first),len(last))):
#             if(first[i]!=last[i]):
#                 return ans
#             ans+=first[i]
#         return ans 

  
# class Solution:
#   def longestCommonPrefix(self, strs: List[str]) -> str:
#     res = ""
#     for a in zip(*strs):
#       if len(set(a)) == 1:
#         res += a[0]
#       else:
#         return res
#     return res


# class Solution:
#   def longestCommonPrefix(self, strs: List[str]) -> str:
#     s = ""
#     l = (len(min(strs, key=len)))
#     strs.sort()
#     for i in range(l):
#       if strs[0][i] == strs[-1][i]:
#         s += strs[0][i]
#       else:
#         break
#     return s

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pre = strs[0]
        
        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]
        
        return pre    


s = Solution()
# print(s.longestCommonPrefix(["a"]))
# print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["fower","flow","flighttest"]))
# print(s.longestCommonPrefix(["c","acc","ccc"]))
