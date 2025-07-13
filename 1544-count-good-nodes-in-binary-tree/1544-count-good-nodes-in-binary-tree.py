# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good = 0
        def dfs(node, largest):
            nonlocal num_good
            if not node:
                return
            if node.val >= largest:
                num_good += 1
            largest = max(largest, node.val)
            dfs(node.left, largest)
            dfs(node.right, largest)
        dfs(root, -math.inf)
        return num_good

        