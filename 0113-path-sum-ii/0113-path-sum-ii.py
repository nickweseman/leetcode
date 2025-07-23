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
            if not node:
                return None
            my_sum = sum_so_far + node.val
            path.append(node.val)
            if not node.left and not node.right:
                if targetSum == my_sum:
                    result.append(path.copy())
            dfs(node.left, my_sum)
            dfs(node.right, my_sum)
            path.pop()
        dfs(root, 0)
        return result