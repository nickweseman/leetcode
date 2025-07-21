# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        path = []
        def backtrack(node, sum_so_far):
            if not node:
                return
            my_sum = sum_so_far + node.val
            path.append(node.val)
            if not node.right and not node.left:
                if my_sum == targetSum:
                    result.append(path.copy())
            else:
                backtrack(node.left, my_sum)
                backtrack(node.right, my_sum)
            path.pop()
        backtrack(root, 0)
        return result