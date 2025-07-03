# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        min1 = root.val
        min2 = math.inf
        def dfs(node) -> None:
            nonlocal min2
            if node:
                if node.val > min1:
                    min2 = min(min2, node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return -1 if min2 == math.inf else min2