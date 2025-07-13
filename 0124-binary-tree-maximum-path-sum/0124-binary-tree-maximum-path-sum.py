# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -math.inf
        def dfs(node) -> int:
            nonlocal max_path
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            max_path = max(max_path, left + right + node.val)
            return max(left, right) + node.val
        dfs(root)
        return max_path
