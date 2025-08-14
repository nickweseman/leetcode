# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        imap = {val:i for i,val in enumerate(inorder)}
        pre_index = 0
        def dfs(left, right):
            nonlocal pre_index
            if left > right:
                return None
            num = preorder[pre_index]
            pre_index += 1
            node = TreeNode(num)
            inorder_index = imap[num]
            node.left = dfs(left, inorder_index - 1)
            node.right = dfs(inorder_index + 1, right)
            return node
        return dfs(0, len(preorder) - 1)