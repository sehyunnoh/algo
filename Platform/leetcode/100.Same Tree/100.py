from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    return self.traverse(p) == self.traverse(q)
    
  def traverse(self, node: Optional[TreeNode]):
    if not node:
      return [None]
    return [node.val] + self.traverse(node.left) + self.traverse(node.right)

n12 = TreeNode(2)
n11 = TreeNode(1, n12)

n2n = TreeNode(None)
n22 = TreeNode(2)
n21 = TreeNode(1, n2n, n22)

s = Solution()
print(s.traverse(n11))
print(s.traverse(n21))
print(s.isSameTree(n11, n21))

# n12 = TreeNode(2)
# n13 = TreeNode(3)
# n11 = TreeNode(1, n12, n13)

# n22 = TreeNode(2)
# n23 = TreeNode(3)
# n21 = TreeNode(1, n22, n23)

# s = Solution()
# print(s.traverse(n11))
# print(s.traverse(n21))
# print(s.isSameTree(n11, n21))
  
  
  