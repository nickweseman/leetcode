# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        num_avg = 0
        def dfs(node) -> Tuple[int, int]: # sum, count
            nonlocal num_avg
            if not node:
                return (0, 0)
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            my_sum = left_sum + right_sum + node.val
            my_count = left_count + right_count + 1
            if my_sum // my_count == node.val:
                num_avg += 1
            return (my_sum, my_count)
        dfs(root)
        return num_avg
