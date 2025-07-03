# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(node) -> Iterator[int]:
            if not node:
                return
            if not node.left and not node.right:
                yield node.val
            else:
                yield from get_leaves(node.left)
                yield from get_leaves(node.right)
        for leaf1, leaf2 in itertools.zip_longest(get_leaves(root1), get_leaves(root2), fillvalue=object()):
            if leaf1 != leaf2:
                return False
        return True