from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#         first, second = [], []
#         self.leafList(root1, first)
#         self.leafList(root2, second)
#         return first == second

#     def leafList(self, root: Optional[TreeNode], arr):
#         if not root:
#             return arr
#         if not root.left and not root.right:
#             arr.append(root.val)
#             return arr
#         arr = self.leafList(root.left, arr)
#         arr = self.leafList(root.right, arr)
#         return arr
    
class Solution:
   def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
       def find_leaf(node):
           if node is None:
               return []
          
           if node.left is None and node.right is None:
               return [node.val]

           left_leaf = find_leaf(node.left)
           right_leaf = find_leaf(node.right)

           return left_leaf + right_leaf
      
       return find_leaf(root1) == find_leaf(root2)    


# seven = TreeNode(7)    
# four = TreeNode(4)
# two = TreeNode(2, seven, four)
# six = TreeNode(6)
# five = TreeNode(5, six, two)
# nine = TreeNode(9)
# eight = TreeNode(8)
# one = TreeNode(1, nine, eight)
# three = TreeNode(3, five, one)
    
# s = Solution()
# print(s.leafSimilar(three, three))

two = TreeNode(2)
one = TreeNode(1, two)

s = Solution()
print(s.leafList(one, one))