# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()
        def dfs(node):
            if node:
                if dfs(node.left):
                    return True
                if k - node.val in nums:
                    return True
                nums.add(node.val)
                if dfs(node.right):
                    return True
        if dfs(root):
            return True
        return False