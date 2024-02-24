from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def preorderTraversal(self, root:Optional[TreeNode]) -> List[int]:
    result = []
    def dfs(root, result):
      if root:
        result.append(root.val)
        dfs(root.left, result)
        dfs(root.right, result)
      else:
        return result
    dfs(root, result)
    return result
  
node3 = TreeNode(3)
node2 = TreeNode(2, node3, None)
node1 = TreeNode(1, None, node2)

s = Solution()
print(s.preorderTraversal(node1))