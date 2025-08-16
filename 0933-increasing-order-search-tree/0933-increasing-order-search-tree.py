# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = None
        prev = None
        def dfs(node):
            nonlocal prev, head
            if node:
                dfs(node.left)
                node.left = None
                if prev:
                    prev.right = node
                else:
                    head = node
                prev = node
                dfs(node.right)
        dfs(root)
        return head