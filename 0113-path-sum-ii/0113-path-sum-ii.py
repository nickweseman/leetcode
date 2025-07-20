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
        def backtrack(node, rolling_sum):
            if not node:
                return
            my_sum = rolling_sum + node.val
            if not node.left and not node.right:
                path.append(node.val)
                if my_sum == targetSum:
                    result.append(path.copy())
                path.pop()
                return
            path.append(node.val)
            backtrack(node.left, my_sum)
            backtrack(node.right, my_sum)
            path.pop()
        backtrack(root, 0)
        return result