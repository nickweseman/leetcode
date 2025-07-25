# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        def dfs(node):
            nonlocal k
            if node:
                result = dfs(node.left)
                if result is not None:
                    return result
                k -= 1
                if k == 0:
                    return node.val
                result = dfs(node.right)
                if result is not None:
                    return result
        return dfs(root)