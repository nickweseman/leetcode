# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return root.val == 1
        left, right = None, None
        if root.left:
            left = self.evaluateTree(root.left)
        if root.right:
            right = self.evaluateTree(root.right)
        if root.val == 2:
            return left or right
        elif root.val == 3:
            return left and right