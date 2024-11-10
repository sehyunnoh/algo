class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def pathSum(self, root: TreeNode, targetSum: int) -> int:
#         def dfs(node, curr_sum):
#             if not node:
#                 return 0
            
#             # Update current prefix sum
#             curr_sum += node.val
#             # Check how many times (curr_sum - targetSum) has appeared so far
#             path_count = prefix_sums.get(curr_sum - targetSum, 0)
            
#             # Update the prefix sums with the current sum
#             prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
            
#             # Recursively search left and right subtrees
#             path_count += dfs(node.left, curr_sum)
#             path_count += dfs(node.right, curr_sum)
            
#             # Backtrack: remove the current sum from the hash map
#             prefix_sums[curr_sum] -= 1
            
#             return path_count
        
#         # Hash map to store the frequency of prefix sums
#         prefix_sums = {0: 1}  # Default prefix sum to handle exact match
#         return dfs(root, 0)

class Solution:
  def pathSum(self, root: TreeNode, targetSum: int) -> int:
    if not root:
      return 0
    
    path_count = self.count_paths_from_node(root, targetSum)
    
    path_count += self.pathSum(root.left, targetSum)
    path_count += self.pathSum(root.right, targetSum)
    
    return path_count
    
    
  def count_paths_from_node(self, node: TreeNode, targetSum: int) -> int:
    if not node:
      return 0
    
    count = 1 if node.val == targetSum else 0
    
    count += self.count_paths_from_node(node.left, targetSum - node.val)
    count += self.count_paths_from_node(node.right, targetSum - node.val)
    
    return count
      
      
s = Solution()
print(s.pathSum([10,5,-3,3,2,null,11,3,-2,null,1], 8))