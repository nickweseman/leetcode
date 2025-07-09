# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_diff = math.inf
        prev = None
        def dfs(node):
            nonlocal min_diff, prev
            if node:
                dfs(node.left)
                if prev:
                    min_diff = min(min_diff, node.val - prev.val)
                prev = node
                dfs(node.right)
        dfs(root)
        return min_diff
