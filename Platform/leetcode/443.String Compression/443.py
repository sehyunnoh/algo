from typing import List


# Time Complexity: O(N)
# Space Complexity: O(1)
# class Solution:
#   def compress(self, chars: List[str]) -> int:
#     if len(chars) == 1: return 1
    
#     result = []
#     char, num = chars[0], 1
#     for i in range(1, len(chars)):
#       if char != chars[i]:
#         result.append(char)
#         if num != 1:
#           result.extend(list(str(num)))
#         char = chars[i]
#         num = 1
#       else:
#         num += 1
#     result.append(char)
#     if num != 1:
#       result.extend(list(str(num)))
      
#     for i in range(len(result)):
#       chars[i] = result[i]
    
#     return len(result)



# Time complexity: O(n*log(n))
# Space complexity: O(1)

class Solution:
  def compress(self, chars: List[str]) -> int:
    def record(chars, index, i, j):
      chars[index] = chars[i]
      index += 1
      if j-i > 1:
        for x in list(str(j-i)):
          chars[index] = x
          index += 1
      return chars, index, i, j
    
    index = i = j = 0
    while (j < len(chars)):
      if chars[i] != chars[j]:
        chars, index, i, j = record(chars, index, i, j)
        i = j
      j += 1
    
    chars, index, i, j = record(chars, index, i, j)
    return index
  

# class Solution:
#   def compress(self, chars: List[str]) -> int:
#     index = i = j = 0
#     while (j < len(chars)):
#       if chars[i] != chars[j]:
#         chars, index, i, j = self.record(chars, index, i, j)
#         i = j
#       j += 1
    
#     chars, index, i, j = self.record(chars, index, i, j)
#     return index
  
#   def record(self, chars, index, i, j):
#     chars[index] = chars[i]
#     index += 1
#     if j-i > 1:
#       for x in list(str(j-i)):
#         chars[index] = x
#         index += 1
#     return chars, index, i, j


# class Solution:
#   def compress(self, chars: List[str]) -> int:
#     index = i = 0  # `index` points to the position where the result will be written, `i` tracks the start of each group

#     for j in range(len(chars)):
#       # If we've reached the end of a group (either end of list or the next char is different)
#       if j + 1 == len(chars) or chars[j] != chars[j + 1]:
#         chars[index] = chars[i]  # Write the character
#         index += 1
#         if j > i:  # If there's more than one occurrence
#           count = str(j - i + 1)  # Get the count of repetitions
#           for c in count:
#             chars[index] = c  # Write each digit of the count
#             index += 1
#         i = j + 1  # Move `i` to the start of the next group

#     return index
  
s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))