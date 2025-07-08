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
        queue = collections.deque([(root, 1)]) # Node, pos
        max_width = -math.inf
        while queue:
            leftmost_pos = math.inf
            rightmost_pos = -math.inf
            for _ in range(len(queue)):
                curr, pos = queue.popleft()
                leftmost_pos = min(leftmost_pos, pos)
                rightmost_pos = max(rightmost_pos, pos)
                if curr.left:
                    queue.append((curr.left, 2 * pos))
                if curr.right:
                    queue.append((curr.right, 2 * pos + 1))
            max_width = max(max_width, rightmost_pos - leftmost_pos + 1)
        return max_width
            