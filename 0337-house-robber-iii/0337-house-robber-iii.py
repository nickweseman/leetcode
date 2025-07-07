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
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            without_me = max(left_rob, left_skip) + max(right_rob, right_skip)
            with_me = left_skip + right_skip + node.val
            return (with_me, without_me)
        return max(dfs(root))