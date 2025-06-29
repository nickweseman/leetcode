# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(root) -> List[TreeNode]:
            if not root:
                return []
            stack = [root]
            result = []
            while stack:
                curr = stack.pop()
                if not curr.right and not curr.left:
                    result.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
            return result
        return leaves(root1) == leaves(root2)