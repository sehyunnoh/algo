from typing import List

class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    add = False
    for i in range(len(digits)-1,-1,-1):
      if digits[i] == 9:
        add = True
        digits[i] = 0
      else:
        add = False
        digits[i] += 1
        break
    if add:
      return ([1] + digits)
    return digits
  
s = Solution()
# print(s.plusOne([1,2,3]))
print(s.plusOne([9]))