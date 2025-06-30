# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: TreeNode, remaining_sum: int) -> None:
            if node:
                remaining_sum -= node.val
                if node.left or node.right:
                    return (dfs(node.left, remaining_sum) 
                        or dfs(node.right, remaining_sum))
                else:
                    if remaining_sum == 0:
                        return True
                    else:
                        return False
            else:
                return False
        return dfs(root, targetSum)