# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result, path = [], []
        def backtrack(node, sum_so_far):
            if node:
                sum_so_far += node.val
                path.append(node.val)
                if not node.left and not node.right:
                    if targetSum == sum_so_far:
                        result.append(path.copy())
                    path.pop()
                    return
                backtrack(node.left, sum_so_far)
                backtrack(node.right, sum_so_far)
                path.pop()
        backtrack(root, 0)
        return result