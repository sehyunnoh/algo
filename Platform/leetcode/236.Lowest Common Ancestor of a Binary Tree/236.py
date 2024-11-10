from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None, p, or q, return root
        if not root or root == p or root == q:
            return root
        
        # Recur for left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both sides are non-null, root is the LCA
        if left and right:
            return root
        
        # Otherwise, return non-null child (either left or right)
        return left if left else right
