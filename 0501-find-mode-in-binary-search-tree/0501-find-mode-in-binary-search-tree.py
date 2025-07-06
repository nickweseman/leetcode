# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = []
        current_freq = max_freq = 0
        current_val = None

        def dfs(node) -> None:
            nonlocal current_freq, max_freq, current_val, modes
            if node:
                dfs(node.left)
                print(f"{node.val} {current_val}")
                if node.val == current_val:
                    print(f"got here")
                    current_freq += 1
                    if current_freq > max_freq:
                        modes = [node.val]
                        max_freq = max(max_freq, current_freq)
                    elif current_freq == max_freq:
                        modes.append(node.val)
                    print(f"got here {modes=}")
                else:
                    current_freq = 1
                    if current_freq > max_freq:
                        modes = [node.val]
                        max_freq = max(max_freq, current_freq)
                    elif current_freq == max_freq:
                        modes.append(node.val)
                    current_val = node.val
                dfs(node.right)
        dfs(root)
        print(f"got here2 {modes=}")
        return modes
        