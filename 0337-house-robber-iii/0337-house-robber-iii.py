# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node) -> Tuple[int, int]: # rob, skip
            if not node:
                return (0, 0)
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            me_rob = left_skip + right_skip + node.val
            me_skip = max(left_skip, left_rob) + max(right_skip, right_rob)
            return (me_rob, me_skip)
        return max(dfs(root))
