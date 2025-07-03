# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node: TreeNode, current_total: int) -> None:
            nonlocal total
            if not node:
                return
            current_total = (current_total << 1) | node.val
            if not node.left and not node.right:
                total += current_total
                return
            dfs(node.left, current_total)
            dfs(node.right, current_total)
        dfs(root, 0)
        return total
