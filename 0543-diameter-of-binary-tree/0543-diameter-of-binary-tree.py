# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = -math.inf
        def dfs(node) -> int:
            nonlocal diameter
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            with_me = left_height + right_height
            without_me = max(left_height, right_height) + 1
            diameter = max(diameter, with_me)
            return without_me
        dfs(root)
        return diameter