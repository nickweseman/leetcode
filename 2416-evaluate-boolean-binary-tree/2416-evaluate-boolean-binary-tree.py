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
        if root.val == 2:
            return (root.left and self.evaluateTree(root.left)) or (root.right and self.evaluateTree(root.right))
        if root.val == 3:
            if root.left:
                left_val = self.evaluateTree(root.left)
                if not left_val:
                    return False
            if root.right:
                right_val = self.evaluateTree(root.right)
                if not right_val:
                    return False
        return True
            
