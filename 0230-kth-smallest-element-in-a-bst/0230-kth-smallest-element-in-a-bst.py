# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_generator(node) -> Iterator[int]:
            if node:
                yield from inorder_generator(node.left)
                yield node.val
                yield from inorder_generator(node.right)
        gen = inorder_generator(root)
        for _ in range(k - 1):
            next(gen)
        return next(gen)