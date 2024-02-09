from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def minDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
      return 0
    if root.left is None and root.right is None:
      return 1
    if root.left is None:
      return self.minDepth(root.right) + 1
    if root.right is None:
      return self.minDepth(root.left) + 1
    return min(self.minDepth(root.left), self.minDepth(root.right)) + 1 
  
  
# n15 = TreeNode(15)
# n7 = TreeNode(7)
# n20 = TreeNode(20, n15, n7)
# n9 = TreeNode(9)
# n3 = TreeNode(3, n9, n20)

# s = Solution()
# print(s.minDepth(n3))

n6 = TreeNode(6)
n5 = TreeNode(5, None, n6)
n4 = TreeNode(4, None, n5)
n3 = TreeNode(3, None, n4)
n2 = TreeNode(2, None, n3)

s = Solution()
print(s.minDepth(n2))

