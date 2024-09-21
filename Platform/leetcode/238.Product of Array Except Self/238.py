from typing import List

# time complexity: O(n)
# space complexity: O(1)

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    nums_len = len(nums)
    left = [1] * nums_len
    right = left[::]
    for i in range(1, nums_len):
      left[i] = left[i-1] * nums[i-1]
      right[nums_len-i-1] = right[nums_len-i] * nums[nums_len-i]
      
    return [(left[i] * right[i]) for i in range(nums_len)]


# time complexity: O(n)
# space complexity: O(1)
  
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        result = [1] * nums_len

        left_product = 1
        for i in range(1, nums_len):
            left_product *= nums[i - 1]
            result[i] = left_product

        right_product = 1
        for i in range(nums_len - 2, -1, -1):
            right_product *= nums[i + 1]
            result[i] *= right_product

        return result      
  
s = Solution()
print(s.productExceptSelf([1,2,3,4]))


# When calculating space complexity, whether or not the output is included depends on the context:

# Auxiliary Space Complexity: This refers to the extra space used by the algorithm, excluding the space used by the input and output. If you're specifically asked about auxiliary space, you do not include the space for the output.

# Total Space Complexity: This considers all the space used by the algorithm, including input, output, and auxiliary space. In this case, the space for the output is included.

# In your case:
# The result array is the output, and since it is necessary to store the final result, it is typically included in the total space complexity.
# So:

# Auxiliary space complexity: O(1) (excluding the output).
# Total space complexity: O(n) (including the output array).