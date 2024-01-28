from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    
    def inorder(root):
      if not root:
        return
      inorder(root.left)
      res.append(root.val)
      inorder(root.right)
    inorder(root)
    
    # def preorder(root):
    #   if not root:
    #     return
    #   res.append(root.val)
    #   preorder(root.left)
    #   preorder(root.right)
    # preorder(root)
    
    # def postorder(root):
    #   if not root:
    #     return
    #   postorder(root.left)
    #   postorder(root.right)
    #   res.append(root.val)
    # postorder(root)
    
    return res
    
n3 = TreeNode(3)
n2 = TreeNode(2, n3)
n1 = TreeNode(1, None, n2)

s = Solution()
print(s.inorderTraversal(n1))


