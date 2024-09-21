from typing import List

class Solution:
  def increasingTriplet(self, nums: List[int]) -> bool:
    first = float('inf')
    second = float('inf')
    
    for x in nums:
      if x <= first:
        first = x
      elif x <= second:
        second = x
      else:
        return True
    return False

# class Solution:
#   def increasingTriplet(self, nums: List[int]) -> bool:
#     arr = []
#     for x in nums:
#       if len(arr) == 0:
#         arr.append(x)
#         continue
      
#       if len(arr) > 0 and arr[-1] < x:
#         arr.append(x)
#       else:
#         arr.pop()
#         if len(arr) > 0 and arr[-1] >= x:
#           arr.pop()
#         arr.append(x)
#         continue
      
#       if len(arr) == 3:
#         return True
    
#     arr = []
#     for x in nums[::-1]:
#       if len(arr) == 0:
#         arr.append(x)
#         continue
#       if len(arr) > 0 and arr[-1] > x:
#         arr.append(x)
#       else:
#         if len(arr) > 0 and arr[-1] <= x:
#           arr.pop()
#         arr.append(x)
#         continue
      
#       if len(arr) == 3:
#         return True
    
#     return False
  
s = Solution()
print(s.increasingTriplet([2,1,5,0,4,6])) # True
print(s.increasingTriplet([20,100,10,12,5,13])) # True
print(s.increasingTriplet([6,7,1,2])) # False
print(s.increasingTriplet([1,1,-2,6])) # False