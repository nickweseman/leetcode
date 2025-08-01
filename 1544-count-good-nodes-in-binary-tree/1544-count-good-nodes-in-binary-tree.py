# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good = 0
        def dfs(node, max_so_far):
            nonlocal num_good
            if node:
                if node.val >= max_so_far:
                    num_good += 1
                    max_so_far = node.val
                dfs(node.left, max_so_far)
                dfs(node.right, max_so_far)
        dfs(root, -math.inf)
        return num_good