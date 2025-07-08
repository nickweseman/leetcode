# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = []
        current_value = None
        current_count = max_freq = 0
        def dfs(node) -> None:
            nonlocal current_value, current_count, modes, max_freq
            if not node:
                return
            dfs(node.left)
            if node.val != current_value:
                current_value = node.val
                current_count = 1
            else:
                current_count += 1
            if current_count > max_freq:
                modes = [node.val]
                max_freq = current_count
            elif current_count == max_freq:
                modes.append(node.val)
            dfs(node.right)
        dfs(root)
        return modes