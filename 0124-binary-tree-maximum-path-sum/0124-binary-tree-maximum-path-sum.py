# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = -math.inf
        def dfs(node) -> int:
            nonlocal max_path_sum
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            with_me = left + right + node.val
            max_path_sum = max(max_path_sum, with_me)
            without_me = max(left, right) + node.val
            return without_me
        dfs(root)
        return max_path_sum