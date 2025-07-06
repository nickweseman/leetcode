# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        max_width = -math.inf
        while queue:
            max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
            for _ in range(len(queue)):
                curr, pos = queue.popleft()
                if curr.left:
                    queue.append((curr.left, pos << 1))
                if curr.right:
                    queue.append((curr.right, (pos << 1) + 1))             
        return max_width
        