# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        queue = collections.deque([root])
        current_depth = 1

        while current_depth < depth - 1:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            current_depth += 1
        
        while queue:
            parent = queue.popleft()
            parent.left = TreeNode(val, left=parent.left)
            parent.right = TreeNode(val, right=parent.right)
        return root
        