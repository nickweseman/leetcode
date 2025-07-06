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
        
        def serialize(node) -> str:
            if not node:
                return "#"
            left = serialize(node.left)
            right = serialize(node.right)

            s = f"{node.val},{left},{right}"
            subtrees[s] += 1
            if subtrees[s] == 2:
                result.append(node)
            return s
        serialize(root)
        return result
        