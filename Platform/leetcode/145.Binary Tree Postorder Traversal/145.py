from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    def dfs(root, result):
      if root is None: return
      dfs(root.left, result)
      dfs(root.right, result)
      result.append(root.val)
    dfs(root, result)
    return result
  



n3 = TreeNode(3)
n2 = TreeNode(2, n3)
n1 = TreeNode(1, None, n2)
  
s = Solution()
print(s.postorderTraversal(n1))