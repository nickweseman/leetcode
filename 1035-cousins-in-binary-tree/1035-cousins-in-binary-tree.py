# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = collections.deque([(root, None)])
        while queue:
            x_node = y_node = None
            for _ in range(len(queue)):
                node, parent = queue.popleft()
                if node.val == x:
                    x_node = node
                    x_parent = parent
                elif node.val == y:
                    y_node = node
                    y_parent = parent

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            if x_node and y_node and x_parent is not y_parent:
                return True
            if x_node or y_node:
                return False
        return False
        