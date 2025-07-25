# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        rolling_sum = 0
        def dfs(node):
            nonlocal rolling_sum
            if not node:
                return None
            dfs(node.right)
            rolling_sum += node.val
            node.val = rolling_sum
            dfs(node.left)
        dfs(root)
        return root