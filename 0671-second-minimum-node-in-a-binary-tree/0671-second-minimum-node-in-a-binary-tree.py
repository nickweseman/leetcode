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
        first = root.val
        second = math.inf
        def dfs(node):
            nonlocal second
            if node:
                if node.val > first:
                    second = min(second, node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return second if second != math.inf else -1