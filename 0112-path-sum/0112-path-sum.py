# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, sum_so_far):
            if not node:
                return False
            new_sum = sum_so_far + node.val
            if not node.left and not node.right and new_sum == targetSum:
                return True
            return dfs(node.left, new_sum) or dfs(node.right, new_sum)
        return dfs(root, 0)