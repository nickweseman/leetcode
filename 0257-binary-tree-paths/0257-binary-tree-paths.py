# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def dfs(node, path_so_far):
            if not node:
                return None
            path_so_far.append(str(node.val))
            if not node.left and not node.right:
                result.append("->".join(path_so_far))
            left = dfs(node.left, path_so_far)
            right = dfs(node.right, path_so_far)
            path_so_far.pop()
        dfs(root, [])
        return result