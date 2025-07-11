# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min1 = root.val
        min2 = math.inf
        def dfs(node) -> int:
            nonlocal min2
            if not node:
                return math.inf
            if node.val > min1:
                min2 = min(min2, node.val)
            left = dfs(node.left)
            right = dfs(node.right)
        dfs(root)
        return -1 if min2 == math.inf else min2
        