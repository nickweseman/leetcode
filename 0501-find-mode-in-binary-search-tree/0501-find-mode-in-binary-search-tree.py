# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = []
        max_freq = cur_freq = 0
        cur_num = None
        def dfs(node):
            nonlocal max_freq, cur_freq, cur_num, modes
            if node:
                dfs(node.left)
                if cur_num is not None and node.val == cur_num:
                    cur_freq += 1
                else:
                    cur_freq = 1
                print(f"{cur_freq=}{max_freq=}{cur_num=}{node.val=}")
                cur_num = node.val
                if cur_freq > max_freq:
                    max_freq = cur_freq
                    modes = [node.val]
                elif cur_freq == max_freq and cur_num != modes[-1]:
                    modes.append(node.val)
                dfs(node.right)
        dfs(root)
        return modes
        