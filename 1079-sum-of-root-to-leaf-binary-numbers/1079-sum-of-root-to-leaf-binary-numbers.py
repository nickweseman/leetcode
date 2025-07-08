# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node, path) -> None:
            nonlocal total
            if not node:
                return None
            num = (path << 1) | node.val
            if not node.right and not node.left:
                total += num
            dfs(node.left, num)
            dfs(node.right, num)
        dfs(root, 0)
        return total
        