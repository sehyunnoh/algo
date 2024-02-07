from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    return self.leftTraverse(root.left) == self.rightTraverse(root.right)
  
  def leftTraverse(self, node: Optional[TreeNode]):
    if node is None:
      return [None]
    return [node.val] + self.leftTraverse(node.left) + self.leftTraverse(node.right)
  
  def rightTraverse(self, node: Optional[TreeNode]):
    if node is None:
      return [None]
    return [node.val] + self.rightTraverse(node.right) + self.rightTraverse(node.left)
  
  
n13 = TreeNode(3)
n14 = TreeNode(4)
n12 = TreeNode(2, n13, n14)

n24 = TreeNode(4)
n23 = TreeNode(3)
n22 = TreeNode(2, n24, n23)

n11 = TreeNode(1, n12, n22)

s = Solution()
print(s.leftTraverse(n11.left))
print(s.rightTraverse(n11.right))
print(s.isSymmetric(n11))