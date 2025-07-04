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
        if root.left:
            if root.left.val != root.val:
                return False
        if root.right:
            if root.right.val != root.val:
                return False
        left_val = self.isUnivalTree(root.left)
        right_val = self.isUnivalTree(root.right)
        return left_val and right_val
