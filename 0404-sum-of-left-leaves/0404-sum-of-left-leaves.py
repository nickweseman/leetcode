# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        left_sum = 0
        def dfs(node, is_left) -> None:
            nonlocal left_sum
            if not node:
                return
            if not node.left and not node.right and is_left:
                left_sum += node.val
            else:
                dfs(node.left, True)
                dfs(node.right, False)
        dfs(root, False)
        return left_sum