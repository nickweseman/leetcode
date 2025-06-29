# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        def serialize(node):
            parts = []
            def preorder(n):
                if not n:
                    parts.append("#")
                    return
                parts.append(str(n.val))
                preorder(n.left)
                preorder(n.right)
            preorder(node)
            return "," + ",".join(parts) + ","
        return serialize(subRoot) in serialize(root)  