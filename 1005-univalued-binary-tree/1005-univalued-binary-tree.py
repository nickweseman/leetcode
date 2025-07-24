# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node, parent_val):
            if not node:
                return True
            if node.val != parent_val:
                return False
            left = self.isUnivalTree(root.left)
            right = self.isUnivalTree(root.right)
            return left and right
        return dfs(root.left, root.val) and dfs(root.right, root.val)