from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_zigzag = 0
        
        def dfs(node, direction, length):
          if not node:
            return
          
          self.max_zigzag = max(self.max_zigzag, length)
          
          if direction == 'left':
            dfs(node.left, "right", length + 1)
            dfs(node.right, "left", 1)
          else:
            dfs(node.right, "left", length + 1)
            dfs(node.left, "right", 1)
            
        dfs(root, "left", 0)
        dfs(root, "right", 0)
        
        return self.max_zigzag