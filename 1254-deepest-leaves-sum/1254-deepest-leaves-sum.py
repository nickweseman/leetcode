# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        while queue:
            level_total = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return level_total
        