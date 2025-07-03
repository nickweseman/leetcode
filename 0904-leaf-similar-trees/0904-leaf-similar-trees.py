# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def tree_iter(root) -> Iterator[int]:
            if not root:
                return
            stack = [root]
            while stack:
                curr = stack.pop()
                if not curr.left and not curr.right:
                    yield curr.val
                else:
                    if curr.left:
                        stack.append(curr.left)
                    if curr.right:
                        stack.append(curr.right)
        for node1, node2 in itertools.zip_longest(tree_iter(root1), tree_iter(root2), fillvalue=object()):
            if node1 != node2:
                return False
        return True
