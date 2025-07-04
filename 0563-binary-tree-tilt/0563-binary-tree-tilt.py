# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_tilt = 0
        def dfs_sum(node) -> None:
            nonlocal total_tilt
            if not node:
                return 0
            left_sum = dfs_sum(node.left)
            right_sum = dfs_sum(node.right)
            total_tilt += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum
        dfs_sum(root)
        return total_tilt