# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        imap = {val: i for i, val in enumerate(inorder)}
        preorder_index = 0
        def dfs(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            num = preorder[preorder_index]
            preorder_index += 1
            inorder_index = imap[num]
            curr = TreeNode(num)
            curr.left = dfs(left, inorder_index - 1)
            curr.right = dfs(inorder_index + 1, right)
            return curr
        return dfs(0, len(preorder) - 1)