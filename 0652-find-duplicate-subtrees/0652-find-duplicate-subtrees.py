# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []
        subtrees = collections.defaultdict(int)
        def serialize(curr):
            if not curr:
                return "#"
            left = serialize(curr.left)
            right = serialize(curr.right)
            s = f"{curr.val},{left},{right}"
            subtrees[s] += 1
            if subtrees[s] == 2:
                result.append(curr)
            return s
        serialize(root)
        return result