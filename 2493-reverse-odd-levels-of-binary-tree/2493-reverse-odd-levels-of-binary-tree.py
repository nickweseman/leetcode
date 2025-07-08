# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []
        queue = collections.deque([root])
        forward = True
        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if not forward:
                left, right = 0, len(level) - 1
                while left < right:
                    level[left].val, level[right].val = level[right].val, level[left].val
                    left += 1
                    right -= 1
            forward = not forward
        return root
            