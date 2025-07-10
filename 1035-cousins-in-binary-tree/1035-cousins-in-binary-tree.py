# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        queue = collections.deque([(root, None)])
        while queue:
            x_curr, y_curr = None, None
            for _ in range(len(queue)):
                curr, parent = queue.popleft()
                if curr.val == x:
                    x_parent = parent
                    x_curr = curr
                elif curr.val == y:
                    y_parent = parent
                    y_curr = curr
                if curr.left:
                    queue.append((curr.left, curr))
                if curr.right:
                    queue.append((curr.right, curr))
            if x_curr and y_curr and x_parent is not y_parent:
                return True
            if x_curr or y_curr:
                return False
        return False
