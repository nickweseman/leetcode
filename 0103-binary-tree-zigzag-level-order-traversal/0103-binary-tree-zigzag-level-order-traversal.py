# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        forward = True
        queue = collections.deque([root])
        result = []
        while queue:
            level = collections.deque()
            for _ in range(len(queue)):
                curr = queue.popleft()
                if forward:
                    level.append(curr.val)
                else:
                    level.appendleft(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            forward = not forward
            result.append(list(level))
        return result