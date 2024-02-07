from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    if not nums:
      return None
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    
    root.left = self.sortedArrayToBST(nums[:mid])
    root.right = self.sortedArrayToBST(nums[mid+1:])
    
    return root
    
  def inorder_traversal(self, node):
    if node:
      self.inorder_traversal(node.left)
      print(node.val, end=" ")
      self.inorder_traversal(node.right)
      
  
  
s = Solution()
# print(s.sortedArrayToBST([-10,-3,0,5,9]))
root = s.sortedArrayToBST([1,2,3,4,5,6,7])
s.inorder_traversal(root)
