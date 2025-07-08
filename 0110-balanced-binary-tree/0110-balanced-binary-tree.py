# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node) -> Tuple[bool, int]: # is_balanced, height
            if not node:
                return (True, 0)
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)
            return (left_balanced and right_balanced and abs(left_height - right_height) <= 1, 
                    max(left_height, right_height) + 1)
        return dfs(root)[0]