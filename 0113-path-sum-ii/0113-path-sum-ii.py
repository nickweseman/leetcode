# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path = []
        result = []
        def dfs(node, sum_so_far):
            if node:
                path.append(node.val)
                total = sum_so_far + node.val
                if not node.left and not node.right and total == targetSum:
                    result.append(path.copy())
                else:
                    dfs(node.left, total)
                    dfs(node.right, total)
                path.pop()
        dfs(root, 0)
        return result