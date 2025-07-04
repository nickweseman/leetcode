# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node, current_sum) -> None:
            nonlocal total
            if node:
                current_sum = (current_sum << 1) | node.val
                if not node.left and not node.right:
                    total += current_sum
                dfs(node.left, current_sum)
                dfs(node.right, current_sum)
        dfs(root, 0)
        return total