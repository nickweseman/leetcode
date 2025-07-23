# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = -math.inf
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        def dfs(node) -> int:
            nonlocal diameter
            if not node:
                return 0
            if not node.left and not node.right:
                return 0
            left_height = dfs(node.left)
            if node.left:
                left_height += 1
            right_height = dfs(node.right)
            if node.right:
                right_height += 1
            with_me = left_height + right_height
            without_me = max(left_height, right_height)
            print(with_me, without_me, diameter)
            diameter = max(diameter, with_me)
            return without_me
        dfs(root)
        return diameter