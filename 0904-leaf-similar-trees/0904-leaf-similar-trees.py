# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(node):
            def dfs(n):
                if n:
                    if not n.left and not n.right:
                        yield n.val
                    yield from dfs(n.left)
                    yield from dfs(n.right)
            yield from dfs(node)
        for leaf1, leaf2 in itertools.zip_longest(get_leaves(root1), get_leaves(root2), fillvalue=object()):
            if leaf1 != leaf2:
                return False
        return True