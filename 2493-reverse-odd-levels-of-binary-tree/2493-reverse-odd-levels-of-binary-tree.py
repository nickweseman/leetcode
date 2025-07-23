# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = collections.deque([(root, 0)])
        while queue:
            level = []
            for _ in range(len(queue)):
                curr, depth = queue.popleft()
                level.append(curr)
                if curr.left:
                    queue.append((curr.left, depth + 1))
                if curr.right:
                    queue.append((curr.right, depth + 1))
            if depth & 1 == 1:
                left, right = 0, len(level) - 1
                while left < right:
                    level[left].val, level[right].val = level[right].val, level[left].val
                    left += 1
                    right -= 1
        return root
            