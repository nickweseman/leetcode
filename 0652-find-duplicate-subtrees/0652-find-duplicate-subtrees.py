# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = collections.defaultdict(int)
        result = []
        def serialize(node):
            if not node:
                return "#"
            left = serialize(node.left)
            right = serialize(node.right)
            tree = f"{node.val},{left},{right}"
            if subtrees[tree] == 1:
                result.append(node)
            subtrees[tree] += 1
            return tree
        serialize(root)
        return result