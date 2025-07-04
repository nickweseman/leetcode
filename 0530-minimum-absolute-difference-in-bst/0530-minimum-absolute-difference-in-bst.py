# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        min_diff = math.inf
        def dfs(node) -> None:
            nonlocal min_diff, prev
            if node:
                dfs(node.left)
                if prev:
                    min_diff = min(min_diff, abs(prev.val - node.val))
                prev = node
                dfs(node.right)
        dfs(root)
        return min_diff
        