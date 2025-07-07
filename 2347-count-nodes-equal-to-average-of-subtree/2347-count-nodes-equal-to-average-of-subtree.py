# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        num_nodes = 0
        def dfs(node) -> Tuple[int, int]:
            nonlocal num_nodes
            if not node:
                return (0, 0)
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            total = left_sum + right_sum + node.val
            count = left_count + right_count + 1
            if total // count == node.val:
                num_nodes += 1
            return (total, count)
        dfs(root)
        return num_nodes