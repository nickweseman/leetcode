# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root or depth == 1:
            return TreeNode(val, left=root)
        queue = collections.deque([(root, 1)])
        while queue:
            for _ in range(len(queue)):
                curr, height = queue.popleft()
                if height == depth - 1:
                    curr.left = TreeNode(val, left=curr.left)
                    curr.right = TreeNode(val, right=curr.right)
                else:
                    if curr.left:
                        queue.append((curr.left, height + 1))
                    if curr.right:
                        queue.append((curr.right, height + 1))
        return root