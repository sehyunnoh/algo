# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#       arr, num = [], 0
#       _, num = self.checkNodes(root, arr, num)
#       return num
    
#     def checkNodes(self, root, arr, num):
#       if not root:
#         return arr, num
#       arr.append(root.val)
#       if all(x <= root.val for x in arr):
#         num += 1
      
#       arr, num = self.checkNodes(root.left, arr, num)
#       arr, num = self.checkNodes(root.right, arr, num)
#       arr.pop()
#       return arr, num
    
class Solution:
   def goodNodes(self, root: TreeNode) -> int:
       def dfs(node, max_num=float('-inf')):
           if node is None:
               return 0
           max_num = max(node.val, max_num)
           return dfs(node.left, max_num) + dfs(node.right, max_num) + int(node.val >= max_num)
      
       return dfs(root)
    
    
three_three = TreeNode(3)
two_one = TreeNode(1, three_three)
three_one = TreeNode(1)
three_five = TreeNode(5)
two_four = TreeNode(4, three_one, three_five)
three = TreeNode(3, two_one, two_four)

s = Solution()
print(s.goodNodes(three))
    
    
