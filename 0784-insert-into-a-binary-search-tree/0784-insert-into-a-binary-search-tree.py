# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def create_tree(node) -> TreeNode:
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = create_tree(node.left)
            elif val > node.val:
                node.right = create_tree(node.right)
            return node
        return create_tree(root)