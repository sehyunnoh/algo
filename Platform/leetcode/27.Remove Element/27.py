from typing import List

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#       dup = nums[::]
#       nums.clear()
#       for x in dup:
#         if x != val:
#           nums.append(x)
#       return len(nums)

# class Solution:
#   def removeElement(self, nums: List[int], val: int) -> int:
#     while val in nums:
#       nums.remove(val)
#     return len(nums)
  
  
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        for v in nums:
            if v!=val:
                nums[j] = v
                j+=1
        return j
      
s = Solution()
# print(s.removeElement([3,2,2,3], 3))  
print(s.removeElement([0,1,2,2,3,0,4,2], 2))  