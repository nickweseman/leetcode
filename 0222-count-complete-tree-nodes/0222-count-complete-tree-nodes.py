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
        def get_height(node) -> int:
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        if left_height == right_height: # left is a perfect subtree
            return (1 << left_height) + self.countNodes(root.right)
        else:                          # right is a perfect subtree
            return (1 << right_height) + self.countNodes(root.left)