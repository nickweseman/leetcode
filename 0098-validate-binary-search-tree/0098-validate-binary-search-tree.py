# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # colorful, blue and green
        def dfs(node):
            if not node:
                return (True, math.inf, -math.inf)
            left_balanced, left_val_low, left_val_high = dfs(node.left)
            right_balanced, right_val_low, right_val_high = dfs(node.right)
            me_balanced = (left_balanced and right_balanced and 
                (left_val_high < node.val) and 
                (node.val < right_val_low))
            me_val_low = min(left_val_low, node.val)
            me_val_high = max(right_val_high, node.val)
            return (me_balanced, me_val_low, me_val_high)
        return dfs(root)[0]