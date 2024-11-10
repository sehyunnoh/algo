from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
          return 0
        
        result = float('-inf')
        max_level = 1
        current_level = 1
        queue = deque([root])
        
        while queue:
          level_size = len(queue)
          acc = 0
          for _ in range(level_size):
            node = queue.popleft()
            acc += node.val 
            
            if node.left:
              queue.append(node.left)
            if node.right:
              queue.append(node.right)
          if acc > result:
            result = acc
            max_level = current_level
            
          current_level += 1
          
        return max_level
          
      
      