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
            leftmost_pos = queue[0][1]
            rightmost_pos = queue[-1][1]
            max_width = max(max_width, rightmost_pos - leftmost_pos + 1)
            for _ in range(len(queue)):
                curr, pos = queue.popleft()
                if curr.left:
                    queue.append((curr.left, 2 * pos))
                if curr.right:
                    queue.append((curr.right, 2 * pos + 1))
        return max_width
