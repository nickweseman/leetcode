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
            # Create a tuple instead of string
            subtree_id = (node.val, left, right)
            subtrees[subtree_id] += 1
            if subtrees[subtree_id] == 2:
                result.append(node)
            return subtree_id
        serialize(root)
        return result
        