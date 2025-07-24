# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def get_height(node):
            if not node:
                return 0
            return 1 + get_height(node.left)
        left = get_height(root.left)
        right = get_height(root.right)
        if left == right:
            return 2 ** left + self.countNodes(root.right)
        else:
            return 2 ** right + self.countNodes(root.left)