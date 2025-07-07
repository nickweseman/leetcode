# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node) -> Tuple[int, int]: # (with_root, without_root)
            if not node:
                return (0, 0)
            left_with_root, left_without_root = dfs(node.left)
            right_with_root, right_without_root = dfs(node.right)
            without_me = max(left_with_root, left_without_root) + max(right_with_root, right_without_root)
            with_me = left_without_root + right_without_root + node.val
            return (with_me, without_me)
        return max(dfs(root))