# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        min1 = root.val
        def dfs(node) -> int:
            if not node:
                return math.inf
            if not node.right and not node.left and node.val != min1:
                if node.val != min1:
                    return node.val
                else:
                    return math.inf
            left = dfs(node.left)
            right = dfs(node.right)
            return min(left, right)
        min2 = dfs(root)
        return -1 if min2 == math.inf else min2
        