# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if val > root.val:
            return TreeNode(val, left=root)
        curr = root
        while curr.right and curr.right.val > val:
            curr = curr.right
        curr.right = TreeNode(val, left=curr.right)
        return root